import json
import os

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

	def handle(self, *args, **options):

		products = Product.objects.all()
		products.delete()
		categories = Category.objects.all()
		categories.delete()

		with open(os.path.abspath('load_data.json'), encoding='UTF-8') as f:
			data = json.load(f)

		categories_to_load = []
		products_to_load = []
		for item in data:
			if item['model'] == 'catalog.category':
				categories_to_load.append(Category(item['pk'], **item['fields']))
			# elif item['model'] == 'catalog.product':
			# 	products_to_load.append(Product(**item['fields']))

		Category.objects.bulk_create(categories_to_load)
		# Product.objects.bulk_create(products_to_load)
