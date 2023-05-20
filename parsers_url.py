from bs4 import BeautifulSoup
from time import sleep
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import geonamescache
import datetime
import re


def parse_of_daylight_hours(region):
    dict_of_cites = {'Амурская область': 'Благовещенск', 'Архангельская область': 'Архангельск', 'Астраханская област\
ь': 'Астрахань', 'Белгородская область': 'Белгород', 'Брянская область': 'Брянск', 'Владимирская область': 'Владими\
р', 'Волгоградская область': 'Волгоград', 'Вологодская область': 'Вологда', 'Воронежская область': 'Воронеж', 'Иван\
овская область': 'Иваново', 'Иркутская область': 'Иркутск', 'Калининградская область': 'Калининград', 'Калужская об\
ласть': 'Калуга', 'Кемеровская область': 'Кемерово', 'Кировская область': 'Киров', 'Костромская область': 'Костром\
а', 'Курганская область': 'Курган', 'Курская область': 'Курск', 'Ленинградская область': 'Санкт-Петербург', 'Липецк\
ая область': 'Липецк', 'Магаданская область': 'Магадан', 'Московская область': 'Москва', 'Мурманская область': 'Мур\
манск', 'Нижегородская область': 'Нижний', 'Новгородская область': 'Новгород', 'Новосибирская область': 'Новосибирс\
к', 'Омская область': 'Омск', 'Оренбургская область': 'Оренбург', 'Орловская область': 'Орел', 'Пензенская област\
ь': 'Пенза', 'Псковская область': 'Псков', 'Ростовская область': 'Ростов-на-Дону', 'Рязанская область': 'Рязан\
ь', 'Самарская область': 'Самара', 'Саратовская область': 'Саратов', 'Сахалинская область': 'Южно-Сахалинск', 'Свер\
дловская область': 'Екатеринбург', 'Смоленская область': 'Смоленск', 'Тамбовская область': 'Тамбов', 'Тверская обла\
сть': 'Тверь', 'Томская область': 'Томск', 'Тульская область': 'Тула', 'Тюменская область': 'Тюмень', 'Ульяновская \
область': 'Ульяновск', 'Челябинская область': 'Челябинск', 'Ярославская область': 'Ярославль', 'Республика Адыге\
я': 'Майкоп', 'Республика Алтай': 'Горно-Алтайск', 'Республика Башкортостан': 'Уфа', 'Республика Бурятия': 'Улан-Уд\
э', 'Республика Дагестан': 'Махачкала', 'Республика Ингушетия': 'Магас', 'Республика Кабардино-Балкария': 'Нальчи\
к', 'Республика Калмыкия': 'Элиста', 'Карачаево-Черкесская республика': 'Черкесск', 'Республика Карелия': 'Петрозав\
одск', 'Республика Коми': 'Сыктывкар', 'Республика Марий Эл': 'Йошкар-Ола', 'Республика Мордовия': 'Саранск', 'Респ\
ублика Саха': 'Якутск', 'Республика Северная Осетия-Алания': 'Владикавказ', 'Республика Татарстан': 'Казань', 'Респ\
ублика Тыва': 'Кызыл', 'Республика Удмуртия': 'Ижевск', 'Республика Хакасия': 'Абакан', 'Республика Чечня': 'Грозны\
    й', 'Республика Чувашия': 'Чебоксары', 'Республика Крым': 'Симферополь', 'Алтайский край': 'Барнаул', 'Забайкальски\
й край': 'Чита', 'Камчатский край': 'Петропавловск-Камчатский', 'Краснодарский край': 'Краснодар', 'Красноярский кр\
ай': 'Красноярск', 'Пермский край': 'Пермь', 'Приморский край': 'Владивосток', 'Ставропольский край': 'Ставропол\
ь', 'Хабаровский край': 'Хабаровск', 'Ненецкий автономный округ': 'Нарьян-Мар', 'Ханты-Мансийский автономный окру\
г': 'Ханты-Мансийск', 'Чукотский автономный округ': 'Анадырь', 'Ямало-Ненецкий автономный округ': 'Салехард', 'Еврейска\
я автономная область': 'Биробиджан'}
    gc = geonamescache.GeonamesCache()
    city_name = dict_of_cites.get(region)
    print(city_name)
    countries = gc.search_cities(city_name, case_sensitive=True)
    id_of_city = countries[0]['geonameid']
    sum_of_day = 0
    avg_summer = datetime.timedelta()
    avg_autumn = datetime.timedelta()
    avg_winter = datetime.timedelta()
    avg_spring = datetime.timedelta()
    for month in range(1, 13):
        url = f'https://dateandtime.info/ru/citysunrisesunset.php?id={id_of_city}&month={month}&year=2023'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.findAll('tbody')[1]
        all_rows = table.findAll('tr')
        mysum = datetime.timedelta()
        for _ in all_rows:
            day_length = _.findAll('td')[4].text
            day_length = day_length[0:5]
            h, m = day_length.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m))
            if 3 <= month <= 5:
                avg_spring += d
            elif 6 <= month <= 8:
                avg_summer += d
            elif 9 <= month <= 11:
                avg_autumn += d
            else:
                avg_winter += d
            mysum += d
            days = mysum.days
        print(f"месяц {month} дней {days} ")
        sum_of_day += days
    avg_autumn = round(avg_autumn / datetime.timedelta(days=91) * 24)
    avg_summer = round(avg_summer / datetime.timedelta(days=92) * 24)
    avg_spring = round(avg_spring / datetime.timedelta(days=92) * 24)
    avg_winter = round(avg_winter / datetime.timedelta(days=90) * 24)
    info_of_days = [avg_summer, avg_winter, avg_spring, avg_autumn, sum_of_day]
    return info_of_days


def parse_of_red_book(name):
    url = f'https://www.plantarium.ru/page/search.html'
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    browser.find_element(By.ID, "taxon-search-value").send_keys(f"{name}")
    browser.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td[2]/input[2]").click()
    browser.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/div[1]/table/tbody/tr/td[2]/a/span").click()
    browser.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td[2]/div/a[1]").click()
    soup = BeautifulSoup(browser.page_source, "lxml")
    table = soup.findAll('tr')[1].findAllNext('td')[1]
    for _ in table.findAll('div', class_='page-section'):
        check_red_book = 0
        if _.find('h2').find('a', href="#redbooks"):
            all_redbooks = _
            check_red_book = 1
            all_redbooks = all_redbooks.findAll('p')
            break
        else:
            pass
    list_of_red_books = []
    if check_red_book:
        for _ in all_redbooks[1:]:
            if _.text[:-7] not in list_of_red_books:
                list_of_red_books.append(_.text[:-7])
    else:
        list_of_red_books = ['Не находится в красной книге']
    return list_of_red_books
