import io
import pdfplumber
from typing import List, Dict, Any
from app.document_processing.text_cleaner import normalize_text

class PDFProcessor:
    @staticmethod
    def extract_text(file_content: bytes) -> List[Dict[str, Any]]:
        """
        Extract text from PDF preserving page numbers.
        Returns a list of dicts with page metadata.
        """
        pages_data = []
        with pdfplumber.open(io.BytesIO(file_content)) as pdf:
            for page_idx, page in enumerate(pdf.pages):
                raw_text = page.extract_text()
                if raw_text:
                    cleaned_text = normalize_text(raw_text)
                    pages_data.append({
                        "page_number": page_idx + 1,
                        "text": cleaned_text
                    })
        return pages_data
