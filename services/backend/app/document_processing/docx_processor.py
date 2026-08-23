import io
import docx
from typing import List, Dict, Any
from app.document_processing.text_cleaner import normalize_text

class DOCXProcessor:
    @staticmethod
    def extract_text(file_content: bytes) -> List[Dict[str, Any]]:
        """
        Extract text from DOCX preserving paragraphs and headings.
        Returns a single 'page' dict as DOCX doesn't have strict physical pages.
        """
        doc = docx.Document(io.BytesIO(file_content))
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text)
                
        cleaned_text = normalize_text("\n".join(full_text))
        return [{
            "page_number": 1,
            "text": cleaned_text
        }]
