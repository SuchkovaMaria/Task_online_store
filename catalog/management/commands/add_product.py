import json
import os

from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add product to the database"

    def handle(self, *args, **kwargs):
        # Удаление созданных продуктов и категорий и добавление тестовых

        Category.objects.all().delete()
        Product.objects.all().delete()

        file_prod = os.path.join("data_fix", "catalog.json")
        with open(file_prod, "r", encoding="utf-8") as f:
            products = json.load(f)

        for product in products:
            if product["model"] == "catalog.category":
                category, created = Category.objects.get_or_create(
                    name=product["fields"]["name"], description=product["fields"]["description"]
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added Product: {category.name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Book already exists: {category.name}"))
            elif product["model"] == "catalog.product":
                product, created = Product.objects.get_or_create(
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    price=product["fields"]["price"],
                    category=category,
                    image=product["fields"]["image"],
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added Product: {product.name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Book already exists: {product.name}"))
