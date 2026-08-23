import uuid
from typing import List, Dict, Any

class DocumentChunker:
    def __init__(self, chunk_size: int = 1000, overlap: int = 200):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_document(self, document_id: str, pages_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Creates overlapping semantic chunks from extracted page data.
        Maintains page metadata.
        """
        chunks = []
        # Flatten text while tracking page boundaries
        # For simplicity in this implementation, we will chunk page by page, 
        # or combine and track offsets.
        
        for page in pages_data:
            page_num = page["page_number"]
            text = page["text"]
            
            start = 0
            text_len = len(text)
            
            while start < text_len:
                end = start + self.chunk_size
                
                # If we are not at the end of the text, try to find a natural break (newline or period)
                if end < text_len:
                    # Look back for a period or newline within the last 100 chars
                    search_range = text[max(start, end-100):end]
                    last_period = search_range.rfind('.')
                    last_newline = search_range.rfind('\n')
                    
                    break_point = max(last_period, last_newline)
                    if break_point != -1:
                        end = max(start, end - 100) + break_point + 1
                
                chunk_text = text[start:end].strip()
                if len(chunk_text) > 50: # Only keep meaningful chunks
                    chunks.append({
                        "id": str(uuid.uuid4()),
                        "document_id": document_id,
                        "page_number": page_num,
                        "text": chunk_text,
                        "char_start": start,
                        "char_end": end
                    })
                
                start = end - self.overlap
                if start < 0 or end >= text_len:
                    break
                    
        return chunks
