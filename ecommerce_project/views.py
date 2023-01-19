from django.shortcuts import render
from store.models import Product

def home(request):

    # Obteniendo los objetos de la base de datos Product
    products = Product.objects.all().filter(is_available=True)

    context = {

        'products': products

    }

    return render(request, "home.html", context)