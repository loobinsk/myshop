from django.contrib import admin
from .models import Category, Product, Comment


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display=['product', 'user', 'text', 'created']
	list_filter=['created', 'product', 'user']
admin.site.register(Comment,CommentAdmin)