from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='logout'),
	path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),
    path('', views.office, name='office'),
]