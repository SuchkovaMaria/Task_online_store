from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class ProductCreateView(CreateView):
    """Класс добавления товара"""
    model = Product
    # Какие поля будут в форме создания
    fields = ["name","description", "image","category", "price"]
    #Куда перенаправляется после того как будет выполнено
    success_url = reverse_lazy("catalog:home")

class ProductDeleteView(DeleteView):
    """Класс удаления товара"""
    model = Product
    success_url = reverse_lazy("catalog:home")

