# 2. Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

import requests


class CurrencyAPI:
    url_for_day = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    url_for_range = "https://bank.gov.ua/NBU_Exchange/exchange_site"

    def get_currency_for_range(self, start, end, currency):
        if int(start) > int(end):
            print("Start date should be before end date.")
            return

        params = {
            "start": start,
            "end": end,
            "valcode": currency,
            "order": "desc",
            "json": "",
        }
        r = requests.get(self.url_for_range, params=params)
        result_list = r.json()
        for record in result_list:
            print(f"{record['exchangedate']}: {round(record['rate'], 2)} ")

    def get_currency_for_day(self, date, currency):
        params = {
            "valcode": currency,
            "date": date,
            "json": "",
        }
        r = requests.get(self.url_for_day, params=params)
        result = r.json()[0]
        print(f"{result['exchangedate']} -> {round(result['rate'], 2)}")


c = CurrencyAPI()
c.get_currency_for_range("20220115", "20220131", "eur")
c.get_currency_for_day("20231203", "eur")
