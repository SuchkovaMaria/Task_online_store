from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import ProductPost


class ProductPostListView(ListView):
    """Контролер для страницы блога ()"""
    model = ProductPost

    def get_queryset(self):
        return ProductPost.objects.filter(ispublic=True)

class ProductPostDetailView(DetailView):
    """Контролер карточки товара"""
    model =  ProductPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object

class ProductPostCreateView(CreateView):
    """Класс добавления отзыва"""
    model = ProductPost
    #Название формы
    template_name = 'blog/blog_create.html'
    # Какие поля будут в форме создания
    fields = ["name","description", "image","product", "ispublic"]
    #Куда перенаправляется после того как будет выполнено
    success_url = reverse_lazy("blog:blog")

class ProductPostUpdateView(UpdateView):
    """Класс редактирования отзыва"""
    model = ProductPost
    template_name = 'blog/blog_create.html'
    fields = ["name", "description", "image", "product", "ispublic"]
    success_url = reverse_lazy("blog:blog")

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail", args=(self.object.pk,))

class ProductPostDeleteView(DeleteView):
    """Класс удаления отзыва"""
    model = ProductPost
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy("blog:blog")