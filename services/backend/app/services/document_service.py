import uuid
from typing import List, Dict, Any, Optional
from app.document_processing.pdf_processor import PDFProcessor
from app.document_processing.docx_processor import DOCXProcessor
from app.document_processing.chunker import DocumentChunker
from app.core.errors import AppError

class DocumentService:
    def __init__(self):
        self.chunker = DocumentChunker()

    def process_document(self, file_content: bytes, filename: str) -> Dict[str, Any]:
        """
        Process a document based on its extension.
        Returns the parsed document metadata and chunks.
        """
        ext = filename.split('.')[-1].lower()
        document_id = str(uuid.uuid4())
        
        if ext == 'pdf':
            pages_data = PDFProcessor.extract_text(file_content)
        elif ext in ['docx', 'doc']:
            pages_data = DOCXProcessor.extract_text(file_content)
        elif ext in ['txt', 'md']:
            # Handle plain text
            text = file_content.decode('utf-8', errors='ignore')
            pages_data = [{"page_number": 1, "text": text}]
        else:
            raise AppError(f"Unsupported file type: {ext}", code="UNSUPPORTED_FILE_TYPE", status_code=400)
            
        chunks = self.chunker.chunk_document(document_id, pages_data)
        
        return {
            "document_id": document_id,
            "filename": filename,
            "total_pages": len(pages_data),
            "total_chunks": len(chunks),
            "chunks": chunks
        }
