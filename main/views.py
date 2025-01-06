from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict[str, str] = {
        'title': 'Home - Главная',\
        'content': 'Магазин мебели Home',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': "Текст об офигенном магазе"
    }
    return render(request, 'main/about.html', context)

