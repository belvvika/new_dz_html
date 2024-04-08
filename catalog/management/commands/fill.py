
from django.core.management import BaseCommand

from catalog.models import Product, Category
class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'milk', 'title': 'milk for family', 'picture': 'Null', 'category': 'category', 'cost': 100, 'date_of_create': 01.01.2004, 'last_modified_date': 01.02.2004}
        ]

        product = []
        for product_item in product_list:
            product.append(Product(**product_item))

        print(product)