from django.shortcuts import render


def index(request):
    data = {"title": "Главная страница", "values": ["яблоко", "груша", "банан"]}
    return render(request, "main/index.html.django", data)


def about(request):
    return render(request, "main/about.html.django", {"title": "О нас"})
