from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    list_products = Phone.objects.all()

    param = request.GET.get('sort')
    if param == 'name':
        list_products = list_products.order_by('name')
    if param == 'min_price':
        list_products = list_products.order_by('price')
    if param == 'max_price':
        list_products = list_products.order_by('-price')

    context = {'list_products': list_products}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.get(slug=slug)
    context = {'product': product}
    return render(request, template, context)
