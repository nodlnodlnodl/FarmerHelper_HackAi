import fitz
import pdfplumber


def del_tire(text):
    return text.replace("-\n", "")


def headers():
    with pdfplumber.open('test.pdf') as pdf:
        text = pdf.pages[0]
        clean_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
        print(clean_text.extract_text())


with fitz.open("test.pdf") as doc:
    text = doc[39].get_text()
    text = del_tire(text)
    print(text)
text