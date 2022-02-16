import fitz

with fitz.open("Section-21 : PDFs/pdf-text/Four-Agreements.pdf") as pdf:
    text = ''
    for page in pdf:
        text = text + page.get_text()
        print(text)
