# 1. Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту https://www.sears.com і буде збирати всі товари із цієї категорії,
# збирати по ним всі можливі дані (бренд, категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл (наприклад, якщо категорія має ID 12345,
# то файл буде називатись 12345_products.csv)
# Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184

import csv
import os
import time

import requests
from fake_useragent import UserAgent


category_id = input("Enter category id: ").strip()


def get_data(category_id, start_index, end_index):
    ua = UserAgent()
    params = {
        "startIndex": start_index,
        "endIndex": end_index,
        "searchType": "category",
        "store": "Sears",
        "storeId": 10153,
        "catGroupId": category_id,
    }
    r = requests.get(
        url="https://www.sears.com/api/sal/v3/products/search",
        headers={"Authorization": "SEARS", "User-Agent": ua.random},
        params=params,
    )
    
    return r.json()


def write_to_csv(category_id, data):
    headers = ["BrandName", "Name", "Category", "FinalPrice"]

    with open(f"{category_id}_products.csv", "a+", encoding="utf-8") as f:
        needs_header = os.stat(f"{category_id}_products.csv").st_size == 0
        writer_obj = csv.writer(f, delimiter=",")

        if needs_header:
            writer_obj.writerow(headers)

        writer_obj.writerow(data)


def find_product_info():
    start_index = 1
    end_index = start_index + 47

    while True:
        data = get_data(category_id, start_index, end_index)

        try:
            product_items = data["items"]
        except KeyError:
            break

        for item in product_items:
            data = [
                item["brandName"],
                item["name"],
                item["category"],
                item["price"]["messageTags"]["finalPrice"],
            ]
            write_to_csv(category_id, data)

        start_index = end_index + 1
        end_index += 47
        time.sleep(15)

    print("Finished!")

find_product_info()
