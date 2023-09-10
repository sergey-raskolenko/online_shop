from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ProductDetailView,contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('item/<int:pk>', ProductDetailView.as_view(), name='item')
]
