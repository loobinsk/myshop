
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', include('homepage.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('admin/', admin.site.urls),
	path('account/', include('account.urls')),
    path('office/', include('PrivateOffice.urls')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
	path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)