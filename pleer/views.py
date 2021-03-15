from django.shortcuts import render
from .models import Song


def index(request):
    tag = request.GET.get('search')
    queryset = Song.objects.all()
    if tag:
        queryset = queryset.filter(tags=int(tag))
    return render(request, "index.html", {'songs': queryset})

