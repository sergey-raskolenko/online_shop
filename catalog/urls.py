from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ProductDetailView, contacts, BlogListView, BlogDetailView, BlogCreateView, \
    BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='item'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('edit_blog/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
]
