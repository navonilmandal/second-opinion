import fitz
from typing import List, Dict, Any
from app.document_processing.text_cleaner import normalize_text

class PDFProcessor:
    @staticmethod
    def extract_text(file_content: bytes) -> List[Dict[str, Any]]:
        """
        Extract text from PDF preserving page numbers using highly-optimized PyMuPDF.
        Returns a list of dicts with page metadata.
        """
        pages_data = []
        doc = fitz.open(stream=file_content, filetype="pdf")
        for page_idx, page in enumerate(doc):
            raw_text = page.get_text()
            if raw_text:
                cleaned_text = normalize_text(raw_text)
                pages_data.append({
                    "page_number": page_idx + 1,
                    "text": cleaned_text
                })
        doc.close()
        return pages_data
