import fitz
import re
import pdfplumber
from utilst import del_tire

list_titles = []

# with fitz.open("atlas.pdf") as doc:
#     for i in range(22, 27):
#         text = doc[i].get_text()
#         text = del_tire(text)
#         print(text)

with pdfplumber.open('atlas.pdf') as pdf:
    for i in range(20, 300):
        text = pdf.pages[i]
        clean_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"] and obj["size"] > 16)
        clean_text_str = str(clean_text.extract_text())
        clean_text_str = re.sub(r"\n", "", clean_text_str)

        print(clean_text_str)
