from django.db import models

from catalog.models import Product


class ProductPost(models.Model):
    name = models.CharField(max_length=100, verbose_name="Краткий отзыв", help_text="Введите краткий отзыв")
    description = models.TextField(verbose_name="Отзыв", blank=True, null=True, help_text="Введите опишите что вам понравилось")
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Товар",
        help_text="Введите название товара",
        related_name="products",
    )
    #путь для сохранения фото товаров
    image = models.ImageField(
        upload_to="data/image_news",
        blank=True,
        null=True,
        verbose_name="Фото новости",
        help_text="Загрузите фото",
    )
    ispublic = models.BooleanField(default=False, verbose_name="статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    view_counter = models.PositiveIntegerField(default=0, verbose_name="Счетчик просмотров")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["product", "description", "created_at"]

    def __str__(self):
        return self.name
