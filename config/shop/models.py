from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category',
						args=[self.slug])


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail',
						args=[self.id, self.slug])

class Comment(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
	text = models.TextField(max_length=1000, )
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)
		verbose_name = 'комментарий'
		verbose_name_plural = 'комментарии'

	def __str__(self):
		return self.text