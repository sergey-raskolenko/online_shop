from django.db import models

from config import settings

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

	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='создатель')

	def __str__(self):
		return f'{self.name}: {self.price} ({self.category})'

	class Meta:
		verbose_name = 'продукт'
		verbose_name_plural = 'продукты'


class Version(models.Model):
	product = models.ForeignKey('Product', on_delete=models.CASCADE)
	version_number = models.IntegerField(verbose_name='Номер версии', unique=True)
	version_name = models.CharField(max_length=100, verbose_name='Название версии')
	is_active = models.BooleanField(default=False, verbose_name='Признак текущей версии')

	def __str__(self):
		return f'Название версии: {self.version_name},№{self.version_number}'

	class Meta:
		verbose_name = 'Версия'
		verbose_name_plural = 'Версии'

