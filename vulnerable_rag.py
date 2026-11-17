import fitz

class VulnerableRAG:
    def __init__(self):
        self.db = []

    def ingest(self, pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() # VULNERABLE: no filtering
        self.db.append(text)
