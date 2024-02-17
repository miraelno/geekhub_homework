from apps.main.celery import app
from apps.products.product_scrapper import start_scrapping
from apps.products.models import Product


@app.task
def save_scrapped_data(product_id):
    data = start_scrapping(product_id)
    Product.objects.update_or_create(id=product_id, defaults={**data})

