from django.shortcuts import render

from django.views.generic import ListView, DetailView

from catalog.models import Product

class ProductListView(ListView):
    """Контролер для главной страницы (список товаров)"""
    model = Product

class ProductDetailView(DetailView):
    """Контролер карточки товара"""
    model =  Product

def contacts(request):
    """Контролер для страницы Контакты"""
    return render(request, "contacts.html")
