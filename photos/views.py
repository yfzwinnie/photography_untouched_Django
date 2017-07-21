from django.shortcuts import render
from .models import Photo

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def trees(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, "trees.html", context)
