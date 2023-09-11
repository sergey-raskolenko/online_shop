# Generated by Django 4.2.4 on 2023-09-11 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Фото')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
