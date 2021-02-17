from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		order = Order.objects.create(
			user = request.user,
			first_name = request.POST['first_name'],
			last_name = request.POST['last_name'],
			email = request.POST['email'],
			address = request.POST['address'],
			postal_code = request.POST['postal_code'],
			city = request.POST['city'],
			)
		for item in cart:
			OrderItem.objects.create(order=order,
									product=item['product'],
									price=item['price'],
									quantity=item['quantity'])
		# очистка корзины
		cart.clear()
		return render(request, 'orders/order/created.html',
                          {'order': order})
	else:
		form = OrderCreateForm
	return render(request, 'orders/order/create.html',
					{'cart': cart, 'form': form})