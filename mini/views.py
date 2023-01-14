from django.shortcuts import render

# Create your views here.
from.models import About


def home(request):
    about=About.objects.last()
    

    return render(request, 'index.html',{

    'about':about,
    })