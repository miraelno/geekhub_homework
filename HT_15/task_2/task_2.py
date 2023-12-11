# 2. Викорисовуючи requests, заходите на ось цей сайт "https://www.expireddomains.net/deleted-domains/" (з ним будьте обережні),
#  вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів - їх там буде десятки тисяч
# (звичайно ураховуючи пагінацію). Всі отримані значення зберігти в CSV файл.

import csv
import os
import time

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


def get_data(params=None):
    ua = UserAgent()

    r = requests.get(
        url="https://www.expireddomains.net/expired-domains/",
        params=params,
        headers={"User-Agent": ua.random},
    )

    return r.content


def write_to_csv(data):
    headers = ["Domain"]

    with open("domains.csv", "a+", encoding="utf-8") as f:
        needs_header = os.stat("domains.csv").st_size == 0
        writer_obj = csv.writer(f)

        if needs_header:
            writer_obj.writerow(headers)

        for row in data:
            writer_obj.writerow([row])


def find_info():
    site_content = get_data()
    counter_page = 25

    while True:
        soup = BeautifulSoup(site_content, features="html.parser")

        rows = soup.find_all("td", "field_domain")
        domain_text_list = []

        for row in rows:
            domain_text_list.append(row.text)

        write_to_csv(domain_text_list)

        if soup.find("a", "next") is None:
            print("Scrapping is finished!")
            return

        params = {"start": counter_page}
        counter_page += 25
        time.sleep(7)
        site_content = get_data(params)


find_info()
