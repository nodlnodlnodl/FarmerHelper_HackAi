import fitz
import pdfplumber
import re
from utils import del_tire


def text_atltas():
    with fitz.open("atlas.pdf") as pdf:
        with open("atltas_txt.txt", "w", encoding="UTF-8") as txt:
            for i in range(18, 618):
                text = pdf[i].get_text()
                text = del_tire(text)
                txt.write(text)


def title_platns():
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
        return list_text


def insert_varible_into_table(name):
    try:
        sqlite_connection = sl.connect('DB1.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_with_param = f"""INSERT INTO Main
                                      (NameCulture)
                                      VALUES (?);"""
        data_tuple = (name,)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Запись успешно вставлена  таблицу", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            
    # clean_text_list = clean_text_str.split('\n')



