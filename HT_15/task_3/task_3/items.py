from scrapy.item import Item, Field


class ExtensionItem(Item):
    name = Field()
    description = Field()
