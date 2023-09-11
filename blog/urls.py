from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('edit_blog/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
]
