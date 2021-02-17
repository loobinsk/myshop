from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

ORDER_STATUS = ((0, 'В обработке'), (1, 'Отправлен'), (2, 'Получен'))

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0, related_name='orders_user')
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.SmallIntegerField(choices=ORDER_STATUS, default=0)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_status(self):
        return ORDER_STATUS[self.status][1]
        
    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity