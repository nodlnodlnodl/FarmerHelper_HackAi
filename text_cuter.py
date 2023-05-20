from pdf_preparation import title_platns


def text_cuter_blocks(title, titlenext):
    with open('atltas_txt.txt', 'r', encoding='utf-8') as fh:
        fulltext = fh.read().split('\n')
        start = title
        end = titlenext
        out_flag = False
        text = ''
        for line in fulltext:
            if line.strip() == start:
                out_flag = True
                continue
            if line.strip() == end:
                break
            if out_flag:
                text += f" {line}"
        return text


