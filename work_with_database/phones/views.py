from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort')
    all_phones_we_have = Phone.objects.all()
    if sort_by == 'low':
        all_phones_we_have = all_phones_we_have.order_by('price')
    elif sort_by == 'high':
        all_phones_we_have = all_phones_we_have.order_by('-price')
    elif sort_by == 'alphabet':
        all_phones_we_have = all_phones_we_have.order_by('name')
    context = {'phone': all_phones_we_have}
    return render(request, template, context = context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug)
    context = {'phone': phone}
    return render(request, template, context = context)
