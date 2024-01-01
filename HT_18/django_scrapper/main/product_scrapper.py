import json

from urllib.parse import urlencode
from fake_useragent import UserAgent
import requests


def start_requests():
    ua = UserAgent()
    headers = {"Authorization": "SEARS", "User-Agent": ua.random}
    params = {"storeName": "Sears", "memberStatus": "G", "zipCode": 10101}
    base_url = "https://www.sears.com/api/sal/v3/products/details/00999941000P"
    
    r = requests.get(url=base_url, headers=headers, params=params)
    print(r.json())

def process_request(self, json_body):
    print('HERE')
    jsonresponse = json.loads(response.text)
    product_info_dict = jsonresponse['productDetail']['softhardProductdetails'][0]
    print(product_info_dict['partNum'])
    print(product_info_dict['descriptionName'])
    print(product_info_dict['salePrice'])
    print(product_info_dict['shortDescription'])
    print(product_info_dict['brandName'])
    print(product_info_dict['seoUrl'])

