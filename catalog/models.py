from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
	name = models.CharField(max_length=50, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание', **NULLABLE)

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name = 'категория'
		verbose_name_plural = 'категории'


class Product(models.Model):
	name = models.CharField(max_length=50, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание', **NULLABLE)
	photo = models.ImageField(upload_to='products/', verbose_name='Превью-фото', **NULLABLE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
	price = models.IntegerField(verbose_name='Цена')
	date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	date_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

	def __str__(self):
		return f'{self.name}: {self.price} ({self.category})'

	class Meta:
		verbose_name = 'продукт'
		verbose_name_plural = 'продукты'
