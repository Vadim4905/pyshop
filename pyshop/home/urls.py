from django.urls import path

from .views import IndexView,  CategoryCreateView,CategoryView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # +
    path("categories/create", CategoryCreateView.as_view(), name="categories_create"),
    path("categories/<pk>", CategoryView.as_view(), name="catalog"), 
]
