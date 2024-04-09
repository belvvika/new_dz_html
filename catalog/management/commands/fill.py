
from django.core.management import BaseCommand

from catalog.models import Product
class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'milk', 'title': 'milk for family', 'picture': 'Null', 'category': 'category', 'cost': 100, 'date_of_create': 2004-1-1, 'last_modified_date': 2004-1-2}
        ]

        product = []
        for product_item in product_list:
            product.append(Product(**product_item))

        print(product)