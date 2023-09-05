from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'objects_list': Product.objects.all(),
        'title': 'Каталог'
    }
    return render(request, 'catalog/index.html', context)


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


def item(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': f'{Product.objects.get(pk=pk).name}',
    }
    return render(request, 'catalog/item.html', context)
