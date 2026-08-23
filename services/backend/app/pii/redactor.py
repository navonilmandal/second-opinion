import re

class PIIRedactor:
    def __init__(self):
        # Basic patterns for demonstration
        self.email_pattern = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
        self.phone_pattern = re.compile(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b")
        # In production, use presidio or advanced NER

    def redact(self, text: str) -> str:
        """Redacts PII from text before it hits the LLM or Vector DB."""
        text = self.email_pattern.sub("[EMAIL_REDACTED]", text)
        text = self.phone_pattern.sub("[PHONE_REDACTED]", text)
        return text
