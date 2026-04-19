from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", contacts, name="contacts"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
