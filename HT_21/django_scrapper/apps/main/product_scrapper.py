import django
django.setup()

from urllib.parse import urljoin

from apps.main.models import Product, Category
from fake_useragent import UserAgent
import requests


def start_scrapping(product_id):
    ua = UserAgent()
    headers = {"Authorization": "SEARS", "User-Agent": ua.random}
    params = {"storeName": "Sears", "memberStatus": "G", "zipCode": 10101}
    base_url = f"https://www.sears.com/api/sal/v3/products/details/{product_id}" 

    r = requests.get(url=base_url, headers=headers, params=params)
    
    try:
        response_json = r.json()
        product_info_dict = response_json['productDetail']['softhardProductdetails'][0]
    except Exception:
        raise Exception 
    
    category_name = product_info_dict['hierarchies']['specificHierarchy'][-1:][0]['name']
    category = get_or_create_category(category_name)[0]
    
    result_dict = {
        "id": product_id,
        "name": product_info_dict['descriptionName'],
        "price": product_info_dict['salePrice'],
        "description": product_info_dict['shortDescription'],
        "brand": product_info_dict['brandName'],
        "category": category,
        "link": urljoin('https://www.sears.com', product_info_dict['seoUrl'])
    }

    return result_dict


def save_scrapped_data(product_id):
    data = start_scrapping(product_id)
    Product.objects.update_or_create(id=product_id, defaults={**data})

def get_or_create_category(category_name):
    return Category.objects.get_or_create(name=category_name)
    
if __name__ == '__main__':
    import django
    django.setup()