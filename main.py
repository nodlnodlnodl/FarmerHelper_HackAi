from pdf_preparation import title_platns, text_atltas
from nlp import found_country
from parsers_url import parse_of_daylight_hours, parse_of_red_book
from pdf_preparation import title_platns, text_atltas
from utils import headers, del_tire
from text_cuter import text_cuter_blocks


# Перегоняем pdf в txt
# text_atltas()
# Берем названия растений из атласа
list_titles_plants = title_platns()
print(list_titles_plants)
for i in range(0, 1):
    print(f'Собираем информацию по {list_titles_plants[i]}')
    # Разбиваем информацию о каждом растении на отдельные куски текста
    text_about_plant = text_cuter_blocks(list_titles_plants[i], list_titles_plants[i+1])
    print(f"Получаем блок текста про нужное нам растение:\n{text_about_plant}\n")
    # Получаем список мест, где хорошо растёт это растение
    list_maybe_cities = found_country(i, list_titles_plants[i], text_about_plant)
    print(f"Список мест роста растения: {list_maybe_cities}")
