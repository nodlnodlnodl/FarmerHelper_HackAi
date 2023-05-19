import fitz
import pdfplumber
import re

# with fitz.open("atlas.pdf") as doc:
#     for i in range(22, 27):
#         text = doc[i].get_text()
#         text = del_tire(text)
#         print(text)
list_text = []
with pdfplumber.open('atlas.pdf') as pdf:
    for i in range(18, len(pdf.pages) - 10):
        text = pdf.pages[i]
        clean_text = text.filter(
            lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"] and obj["size"] > 16)
        clean_text_str = str(clean_text.extract_text())
        if clean_text_str != '':
            clean_text_str = re.sub(r'\n.*', '', clean_text_str)
            list_text.append(clean_text_str)
    print(list_text)
    # clean_text_list = clean_text_str.split('\n')
