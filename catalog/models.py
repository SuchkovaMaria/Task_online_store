from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория", help_text="Введите название категории")
    description = models.TextField(verbose_name="Описание", blank=True, null=True, help_text="Введите описание товара")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Товар", help_text="Введите название товара")
    description = models.TextField(verbose_name="Описание", blank=True, null=True, help_text="Введите описание товара")

    #путь для сохранения фото товаров
    image = models.ImageField(
        upload_to="data/image_product",
        blank=True,
        null=True,
        verbose_name="Фото товара",
        help_text="Загрузите фото товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        help_text="Введите название товара",
        related_name="categories",
    )
    price = models.FloatField(verbose_name="Цена", help_text="Укажите цену товара")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "price", "created_at"]

    def __str__(self):
        return self.name
