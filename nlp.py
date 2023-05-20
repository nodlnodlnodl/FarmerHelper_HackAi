import spacy
from spacy.lang.ru import Russian
from spacy import displacy


def found_country(i, title, text):
    nlp = spacy.load('ru_core_news_lg')
    dict_nameplant = {}
    # Берем страну из Ареала
    s = text
    list_country = []
    start = "Ареал."
    end = "Экология."
    out_flag = False
    text = ''
    for word in s.split():
        if word.strip() == start:
            out_flag = True
            continue
        if word.strip() == end:
            break
        if out_flag:
            text += f" {word}"
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ['LOC', 'GPE']:
            list_country.append(ent.lemma_)
    return list_country



