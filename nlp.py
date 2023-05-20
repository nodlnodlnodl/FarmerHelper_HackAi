import spacy
from spacy.lang.ru import Russian
from spacy import displacy
from pdf_preparation import title_platns


nlp = spacy.load('ru_core_news_lg')
dict_nameplant = {}
for i in range(0, 1):  # 190
    # with open(f"txt_plants_i/{i}_{title_platns()[i]}.txt", "r", encoding="UTF-8") as file:
    with open(f"txt_plants_i/0_АДЕНОСТИЛЕС РОМБОЛИСТНЫЙ.txt", "r", encoding="UTF-8") as file:
        # Берем страну из Ареала
        s = file.read()
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
                print(list_country)
        dict_nameplant['ДЕНОСТИЛЕС РОМБОЛИСТНЫЙ'] = list_country
        print(dict_nameplant)

