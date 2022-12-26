from django.shortcuts import render
from.models import Posts

# Create your views here.

def post_list(request):
    all = Posts.objects.all()
    return render (request, 'posts.html', {'data':all})


def post_detail(request,id):
    post = Posts.objects.get(id=id)
    return render(request, 'single.html', {'data':post})