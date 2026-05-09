from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """Контролер для главной страницы (список товаров)"""

    model = Product


class ProductDetailView(DetailView):
    """Контролер карточки товара"""

    model = Product


class ProductCreateView(CreateView):
    """Класс добавления товара"""

    model = Product
    # Название формы
    template_name = "catalog/product_form.html"
    # Какие поля будут в форме создания
    form_class = ProductForm
    # Куда перенаправляется после того как будет выполнено
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Автозаполнение
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    """Класс редактирования товара"""

    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=(self.object.pk,))


class ProductDeleteView(DeleteView):
    """Класс удаления товара"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ContactsTemplateView(TemplateView):
    """Контролер для страницы Контакты"""

    template_name = "catalog/contacts.html"


class PublicProductView(LoginRequiredMixin, View):
    """Контроллер для публикации товара"""

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для публикации товара.")

        product.status = True
        product.save()

        return redirect("catalog:home")