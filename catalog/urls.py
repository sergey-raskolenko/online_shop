from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ProductDetailView, contacts, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='item'),
    path('create/', ProductCreateView.as_view(), name='create_item'),
    path('update/item/<int:pk>/', ProductUpdateView.as_view(), name='update_item'),
    path('delete/item/<int:pk>/', ProductDeleteView.as_view(), name='delete_item'),
]
