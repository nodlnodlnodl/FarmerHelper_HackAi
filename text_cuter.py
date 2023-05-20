from pdf_preparation import title_platns


with open('atltas_txt.txt', 'r', encoding='utf-8') as fh:
    for i in range(0, 190): #190
        fulltext = fh.read()
        with open(f"txt_plants_i/{i}_{title_platns()[i]}.txt", "w", encoding="UTF-8") as file:
            start = title_platns()[i]
            end = title_platns()[i+1]
            out_flag=False
            text = ''
            for line in fulltext:
                if line.strip() == start:
                    out_flag = True
                    continue
                if line.strip() == end:
                    break
                if out_flag:
                    text += line
            print(text)
            file.write(f'{text}')

