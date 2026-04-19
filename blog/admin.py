from django.contrib import admin

from blog.models import ProductPost


@admin.register(ProductPost)
class ProductPostAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product", "description", "ispublic")
    list_filter = ("product",)
    search_fields = ("name", "description", "view_counter" )
    list_editable = ("product","name", "description")
