from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import white, black

def create_test_pdf(filename="test_doc.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFillColor(black)
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, "Project X Status: On track.")
    c.setFillColor(white)
    c.setFont("Helvetica", 1)
    c.drawString(100, 600, "INJECTION_TEST_MARKER")
    c.save()

if __name__ == "__main__":
    create_test_pdf()
