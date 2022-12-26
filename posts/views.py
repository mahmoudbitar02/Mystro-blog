from django.shortcuts import render
from.models import Posts
from .forms import PostForm

# Create your views here.

def post_list(request):
    all = Posts.objects.all()
    return render (request, 'posts.html', {'data':all})


def post_detail(request,id):
    post = Posts.objects.get(id=id)
    return render(request, 'single.html', {'data':post})



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        form = PostForm()
    return render(request, 'create.html', {'form':form})