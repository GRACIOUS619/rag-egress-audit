import fitz
import unicodedata
import re

class Sanitizer:
    def __init__(self):
        self.invisible = re.compile(r'[\u200B-\u200F\u202A-\u202E\u2060-\u206F\uFEFF]')

    def sanitize_text(self, text):
        text = unicodedata.normalize('NFKC', text)
        return self.invisible.sub('', text)

    def extract_pdf_safely(self, pdf_path):
        doc = fitz.open(pdf_path)
        safe_text = []
        for page in doc:
            d = page.get_text("dict")
            for block in d["blocks"]:
                if block["type"] != 0: continue
                for line in block["lines"]:
                    for span in line["spans"]:
                        if span["size"] < 5.0: continue # Strip tiny font
                        safe_text.append(span["text"])
        return self.sanitize_text(" ".join(safe_text))
