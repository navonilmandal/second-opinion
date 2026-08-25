from app.ai.llm.mock import MockLLMProvider
from app.ai.llm.openrouter import OpenRouterLLMProvider
from app.pii.redactor import PIIRedactor
from app.ai.schemas import ClauseAnalysisResult
from app.core.config import settings
from typing import Dict, Any

class RAGOrchestrator:
    def __init__(self):
        if settings.LLM_PROVIDER.lower() == "openrouter":
            from app.ai.llm.openrouter import OpenRouterLLMProvider
            self.llm = OpenRouterLLMProvider()
        else:
            from app.ai.llm.mock import MockLLMProvider
            self.llm = MockLLMProvider()
            
        self.redactor = PIIRedactor()
        
        # Initialize RAG components
        from app.ai.rag.qdrant_client import QdrantService
        from app.ai.embeddings.fastembed_provider import FastEmbedProvider
        
        self.qdrant = QdrantService()
        self.embedder = FastEmbedProvider()
        
    async def analyze(self, document_id: str, query: str) -> ClauseAnalysisResult:
        """
        Orchestrates the entire RAG flow:
        1. Embed the query
        2. Retrieve most relevant chunks from Qdrant
        3. Redact PII (if needed)
        4. Construct context and prompt
        5. Call LLM for structured analysis
        """
        # 1. Embed query
        query_embedding = (await self.embedder.generate_embeddings([query]))[0]
        
        # 2. Retrieve top chunks
        chunks = self.qdrant.search_chunks(document_id, query_embedding, limit=5)
        
        if not chunks:
            # Fallback if no chunks found
            context = "No relevant document text found."
        else:
            # Combine text and redact PII
            raw_context = "\n\n".join([f"Page {c.get('page_number')}: {c.get('text')}" for c in chunks])
            context = self.redactor.redact(raw_context)
            
        # 3. Call LLM provider
        prompt = f"Query: {query}\n\nRelevant Document Context:\n{context}\n\nAnalyze the context and respond strictly with the JSON schema requested."
        
        raw_result = await self.llm.analyze_clause(prompt)
        
        # 4. Validate against strict Pydantic schema
        try:
            return ClauseAnalysisResult(**raw_result)
        except Exception as e:
            print("ValidationError from LLM output:", str(e))
            return ClauseAnalysisResult(
                chunk_id="error",
                risk_level="medium",
                risk_score=50,
                title="Analysis Error",
                summary="The AI returned an invalid response format. We could not parse the risk score.",
                why_flagged="Invalid AI Response: " + str(e)[:100],
                recommendation="Please try analyzing the policy again.",
                confidence="low",
                evidence=[]
            )
