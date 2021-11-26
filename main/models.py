from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=50, verbose_name='Название')
	description = models.TextField(verbose_name='Описание')
	material = models.CharField(null=True, max_length=50, verbose_name='Материал изделия')
	length = models.IntegerField(null=True, verbose_name='Длина изделия')
	slug = models.SlugField(unique=True, verbose_name='Ссылка')
	img = models.ImageField(blank=True, verbose_name='Фото')
	price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Товары'
		verbose_name_plural='Товары'

	def get_absolute_url(self):
		return self.slug
