# 2. Створіть програму для отримання курсу валют за певний період. 
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

import requests


class CurrencyAPI:
    
    def __init__(self):
        self.url_for_day = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
        self.url_for_range = 'https://bank.gov.ua/NBU_Exchange/exchange_site'

    def get_currency_for_range(self, start, end, currency):
        if start > end:
            print('Start date should be before end date.')
            return
        
        r = requests.get(f"{self.url_for_range}?start={start}&end={end}&valcode={currency}&exchangedate&order=desc&json")
        result_list = r.json()
        for record in result_list:
            print(f"{record['exchangedate']}: {round(record['rate'], 2)} ")

    def get_currency_for_day(self, date, currency):
        r = requests.get(f'{self.url_for_day}?valcode={currency}&date={date}&json')
        result = r.json()[0]
        print(f"{result['exchangedate']} -> {round(result['rate'], 2)}")
        

c = CurrencyAPI()
c.get_currency_for_range('20220115', '20220131', 'eur')
c.get_currency_for_day('20231203', 'eur')
