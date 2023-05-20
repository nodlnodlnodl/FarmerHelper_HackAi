import fitz
import pdfplumber


def del_tire(text):
    return text.replace("-\n", "")


def headers():
    with pdfplumber.open('test.pdf') as pdf:
        text = pdf.pages[0]
        clean_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
        print(clean_text.extract_text())


def search_region(city):
  for i in range(len(search_region.russia)):
    if city == search_region.russia[i]['city']:
      return search_region.russia[i]['region']

def search(array):
    for i in range(len(array)):
        for j in range(len(search_region.russia)):
            if array[i] == search_region.russia[j]['region']:
                return search_region.russia[j]['region']
