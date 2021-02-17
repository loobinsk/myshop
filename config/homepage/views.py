from django.shortcuts import render
from shop.models import Product

# Create your views here.
def index(request):
	latest_products = Product.objects.all().order_by('-created')[:3]
	cheap_products = Product.objects.all().order_by('price')[:3]
	template = 'homepage.html'
	context = {
		'latest_products': latest_products,
		'cheap_products': cheap_products,
	}
	return render(request, template, context)