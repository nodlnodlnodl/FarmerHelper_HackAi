from bs4 import BeautifulSoup
from time import sleep
import requests
import datetime
import re

def parse_of_daylight_hours(city):
    id_of_city = 553915
    mysum = datetime.timedelta()
    for month in range(1, 13):
        url = f'https://dateandtime.info/ru/citysunrisesunset.php?id={id_of_city}&month={month}&year=2023'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.findAll('tbody')[1]
        all_rows = table.findAll('tr')
        for _ in all_rows:
            day_length = _.findAll('td')[4].text
            h, m, s = day_length.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            mysum += d
            days = mysum.days
        print(f"месяц {month} дней {days} ")

def parse_of_red_book():
    pass


parse_of_daylight_hours("Пенза")
