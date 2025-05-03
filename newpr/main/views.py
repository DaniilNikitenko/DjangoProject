from django.shortcuts import render


def index(request):
    return render(request, "main/index.html.django")


def about(request):
    return render(request, "main/about.html.django")
