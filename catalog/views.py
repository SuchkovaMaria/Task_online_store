from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    """Контролер для главной страницы"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def contacts(request):
    """Контролер для страницы Контакты"""
    return render(request, "contacts.html")

def product_info(request, pk):
    """Контролер карточки товара"""
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_info.html", context)

