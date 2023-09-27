from django.db import models
from django.utils import timezone

from catalog.models import NULLABLE


class Blog(models.Model):
	title = models.CharField(max_length=100, verbose_name='Заголовок', **NULLABLE)
	slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
	body = models.TextField(verbose_name='Содержимое', **NULLABLE)
	image = models.ImageField(upload_to='blog/', verbose_name='Фото', **NULLABLE)
	creation_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
	is_published = models.BooleanField(verbose_name='Опубликован', default=False)
	views_count = models.IntegerField(verbose_name='количество просмотров', default=0)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name = 'блог'
		verbose_name_plural = 'блоги'
