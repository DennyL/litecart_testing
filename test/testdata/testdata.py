from datetime import datetime
from test.generators import generators


class Product:
    """
       used to create product instances
    """
    def __init__(self):

        self.date = datetime.now()

        # GENERAL
        self.product_name = generators.item_names_generator(prefix='item_', length=8)
        self.code = generators.item_codes_generator(prefix='#', length=3)
        self.sku = generators.item_codes_generator(prefix='SKU_', length=4)
        self.mpn = generators.item_codes_generator(prefix='MPN_', length=5)
        self.gtin = generators.item_codes_generator(prefix='GTIN_', length=5)
        self.taric = generators.item_codes_generator(prefix='TARIC_', length=5)
        self.manufacturer = '1'
        self.date_valid_from = f'{self.date.day}/{self.date.month}/{self.date.year}'
        self.date_valid_to = f'{self.date.day}/{self.date.month}/{self.date.year + 1}'
        self.keywords = self.product_name[:8]
        self.image = generators.item_picture_provider()

        # INFORMATION
        self.short_description = 'Nice thing to purchase'
        self.description = 'Superb quality goods from Ukrainian farmers'
        self.technical_data = 'Contact the dealer'
        self.head_title = 'Head Title'
        self.meta_description = 'Meta description is missing'

        # PRICES
        self.tax_class = 'first'
        self.purchase_price = '50'
        self.purchase_price_currency = 'USD'
        self.price_usd = '50'

    def __str__(self) -> str:
        """ :returns a string with all the fields of a product instance """
        product_info = []
        for k, v in self.__dict__.items():
            product_info.append(f'\n{k.upper()} : {str(v)}')
        return ''.join(product_info)
