from django.shortcuts import render

# Create your views here.
from.models import About, Skills, Education, Experience, Service


def home(request):
    about=About.objects.last()
    coding_skill=Skills.objects.filter(type='Coding')
    design_skill=Skills.objects.filter(type='Design')
    education =Education.objects.all()
    experience = Experience.objects.all()
    service= Service.objects.all()
    

    return render(request, 'index.html',{

    'about':about,
    'coding_skill':coding_skill,
    'design_skill':design_skill,
    'education':education,
    'experience':experience,
    'service':service,


    })