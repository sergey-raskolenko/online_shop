from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from catalog.models import Product


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Каталог'
    }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['objects_list'] = Product.objects.all()
        return context_data


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['object'] = product_item
        context_data['title'] = f'{product_item.name}'
        return context_data

