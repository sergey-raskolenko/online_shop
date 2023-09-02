from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
	name = models.CharField(max_length=50, verbose_name='Наименование', **NULLABLE)
	description = models.TextField(verbose_name='Описание')

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name = 'категория'
		verbose_name_plural = 'категории'
