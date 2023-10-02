from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ProductDetailView, contacts, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('item/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='item'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create_item'),
    path('update/item/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='update_item'),
    path('delete/item/<int:pk>/', ProductDeleteView.as_view(), name='delete_item'),
]
