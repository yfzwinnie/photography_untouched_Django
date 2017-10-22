from django.shortcuts import render
from .models import Photo

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def gallery(request):
    queryset = Photo.objects.filter(category='G')
    context = {
        "photos": queryset,
    }
    return render(request, "gallery.html", context)

def trees(request):
    queryset = Photo.objects.filter(category='N')
    context = {
        "photos": queryset,
    }
    return render(request, "trees.html", context)

def city(request):
    queryset = Photo.objects.filter(category='C')
    context = {
        "photos": queryset,
    }
    return render(request, "city.html", context)

def portraits(request):
    queryset = Photo.objects.filter(category='P')
    context = {
        "photos": queryset,
    }
    return render(request, "portraits.html", context)

def animals(request):
    queryset = Photo.objects.filter(category='A')
    context = {
        "photos": queryset,
    }
    return render(request, "animals.html", context)
