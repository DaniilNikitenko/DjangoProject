from django.shortcuts import render
from .models import Articals


def news(request):
    news = Articals.objects.order_by("-date")
    return render(request, "news/news.html.django", {"news": news})
