import factory

from apps.products import models 


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
        
        
    name = 'Test category'
    
    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product
        
    id = 'A122177272'
    name = 'Test product name'
    price = 10
    description = 'Some product description'
    brand = 'Test product brand'
    category = factory.SubFactory(CategoryFactory)
    link = 'https://www.sears.com/costway-hw71608-costway-2-seat-porch-swing-bench-acacia-wood-chair-with-2-hanging-hemp-ropes-for-backyard/p-A122177272'