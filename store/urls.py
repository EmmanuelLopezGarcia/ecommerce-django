from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name='store'),
    # Se define una url dinamica
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    # Se define otra url para los detalles de un producto
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]