from django.urls import path

from .views import IndexView, catalog, CategoryCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # +
    path("catalogs/", catalog, name="catalogs"),
    path("categories/create", CategoryCreateView.as_view(), name="categories_create"),
]
