from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ContactsTemplateView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, PublicProductView, ProductCategoryListView
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("catalog/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("catalog/create/", ProductCreateView.as_view(), name="catalog_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="catalog_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="catalog_delete"),
    path("catalog/<int:pk>/public/", PublicProductView.as_view(), name="catalog_public"),
    path("catalog/<int:pk>/product_category/", ProductCategoryListView.as_view(), name="product_category"),
]
