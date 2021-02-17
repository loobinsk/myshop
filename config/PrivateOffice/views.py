from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from orders.models import Order, OrderItem
# Create your views here.
def office(request):
	orders = Order.objects.filter(user=request.user)
	context = {
		'orders': orders,
	}
	return render(request, 'office.html', context)