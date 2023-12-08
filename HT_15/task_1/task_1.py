# 1. Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту https://www.sears.com і буде збирати всі товари із цієї категорії, 
# збирати по ним всі можливі дані (бренд, категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл (наприклад, якщо категорія має ID 12345,
# то файл буде називатись 12345_products.csv)
# Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184

import json

import requests
from fake_useragent import UserAgent


def get_data(category_id):
    ua = UserAgent()
    params = {
        "searchType": "category",
        "store": "Sears",
        "storeId": 10153,
        "catGroupId": 5000928,
    }
    r = requests.get(
        url='https://www.sears.com/api/sal/v3/products/search',
        headers={"Authorization": "SEARS",
                "User-Agent": ua.random},
        params=params,
    )

    with open('test.json', 'w') as f:
        f.write(json.dumps(r.json(), indent=4))
    
    return r.json()


def get_mocked_data():
    with open('test.json', 'r') as f:
        data = json.loads(f.read())
    
    return data


# get_data()
print(get_mocked_data())