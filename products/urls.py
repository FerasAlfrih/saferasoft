from django.urls import path
from . import views

urlpatterns = [

    path('', views.product, name='products'),
    path('newproduct/', views.newproduct, name='newproduct'),
    path('products/details/<int:pk>/', views.product_details, name='product_details'),

]