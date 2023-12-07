# 2. Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

from datetime import datetime
import requests


class CurrencyAPI:
    url_for_day = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    url_for_range = "https://bank.gov.ua/NBU_Exchange/exchange_site"

    def validate_date(self, dates):
        formatted_dates = []
        for date in dates:
            date_format = '%Y%m%d'
            try:
                formatted_date = datetime.strptime(date, date_format)
                formatted_dates.append(datetime.strftime(formatted_date, date_format))
            except ValueError:
                print(f'Invalid date format: {date}')
                return
        return formatted_dates

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

    def user_interaction(self):
        date_from_user = input("Enter one date or date range in format YYYYMMDD YYYYMMDD: ").strip().split(' ')
        formatted_dates_list = self.validate_date(date_from_user)

        if(formatted_dates_list == None):
            return
        
        if len(date_from_user) == 1:
            currency = input('Enter currency literal code: ')
            self.get_currency_for_day(formatted_dates_list[0], currency)
        else:
            date_from, date_to = formatted_dates_list
            currency = input('Enter currency literal code: ')
            self.get_currency_for_range(date_from, date_to, currency)


c = CurrencyAPI()
c.user_interaction()
