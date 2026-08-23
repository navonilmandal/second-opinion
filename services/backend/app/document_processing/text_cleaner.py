import re
import unicodedata

def normalize_text(text: str) -> str:
    """Normalize unicode and remove excessive whitespace."""
    if not text:
        return ""
    # Normalize unicode
    text = unicodedata.normalize("NFKC", text)
    # Replace newlines with spaces or keep them based on context
    text = re.sub(r'\r\n', '\n', text)
    # Remove multiple spaces
    text = re.sub(r'[ \t]+', ' ', text)
    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()
