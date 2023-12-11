from scrapy.item import Item, Field


class ExtensionItem(Item):
    id = Field()
    name = Field()
    description = Field()
