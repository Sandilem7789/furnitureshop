from django.urls import path
from .views import logout_view 
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('orders/', views.order_history, name='order_history'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='store/login.html'), name='login'), 
]
