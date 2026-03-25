from django.shortcuts import render

def home(request):
    """Контролер для главной страницы"""
    return render(request, 'home.html')

def contacts(request):
    """Контролер для страницы Контакты"""
    return render(request, "contacts.html")
