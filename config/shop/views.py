from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Comment
from .forms import CommentForm
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
		paginator = Paginator(products, 8)
	return render(request,
					'shop/product/list.html',
					{'category': category,
					'categories': categories,
					'products': products,
					})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	comments = Comment.objects.filter(product=product).order_by('-created')
	if request.method == 'POST':
		new_comment = Comment()
		new_comment.product = product
		new_comment.user = request.user
		new_comment.text = request.POST['comment_text']
		new_comment.save()
		return redirect(request.path)
	else:
		comment_form = CommentForm()

	return render(request,
					'shop/product/detail.html',
					{'product': product, 
					'comments': comments

					})