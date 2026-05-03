from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    ProductPostListView,
    ProductPostDetailView,
    ProductPostUpdateView,
    ProductPostDeleteView,
    ProductPostCreateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("productpost_list/", ProductPostListView.as_view(), name="blog"),
    path("blog/<int:pk>/", ProductPostDetailView.as_view(), name="blog_detail"),
    path("blog/create/", ProductPostCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", ProductPostUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", ProductPostDeleteView.as_view(), name="blog_delete"),
]
