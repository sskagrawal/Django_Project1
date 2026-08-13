from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def acrepair(request):
    return render(request, 'ac-repair-service.html')


def tiles(request):
    return render(request, 'tiles.html')


def realstate(request):
    return render(request, 'realestate.html')
