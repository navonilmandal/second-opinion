from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from app.services.document_service import DocumentService
from pydantic import BaseModel

router = APIRouter()
doc_service = DocumentService()

class UploadResponse(BaseModel):
    document_id: str
    message: str
    num_chunks: int

@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """Uploads a PDF or DOCX file, processes it, and chunks the text."""
    if not file.filename.endswith(('.pdf', '.docx', '.txt')):
        raise HTTPException(status_code=400, detail="Only PDF, DOCX, and TXT files are supported")
        
    temp_path = f"/tmp/{file.filename}"
    # In Windows environment, fallback to a local temp dir
    if os.name == 'nt':
        os.makedirs("temp_uploads", exist_ok=True)
        temp_path = f"temp_uploads/{file.filename}"
        
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        with open(temp_path, "rb") as f:
            file_content = f.read()
            
        result = doc_service.process_document(file_content, file.filename)
        document_id = result["document_id"]
        chunks = result["chunks"]
        
        # Initialize dependencies
        from app.ai.embeddings.fastembed_provider import FastEmbedProvider
        from app.ai.rag.qdrant_client import QdrantService
        
        embedder = FastEmbedProvider()
        qdrant = QdrantService()
        
        # Extract texts for embedding
        texts = [chunk["text"] for chunk in chunks]
        
        # Generate embeddings and upsert
        if texts:
            embeddings = await embedder.generate_embeddings(texts)
            qdrant.upsert_chunks(document_id, chunks, embeddings)
        
        return UploadResponse(
            document_id=document_id,
            message="Document successfully processed, chunked, and indexed.",
            num_chunks=len(chunks)
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
