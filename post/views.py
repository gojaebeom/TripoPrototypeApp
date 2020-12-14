from typing import ContextManager
from post.models import Post
from django.shortcuts import redirect, render
from category.models import Category
from django.views.decorators.http import require_GET, require_POST

# Create your views here.
@require_GET
def index(request):
    post_list = Post.objects.all()
    return render(request, 'post/index.html', {'post_list':post_list})


def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/show.html', {'post':post})


@require_GET
def create(request):
    if not request.user.is_authenticated:
        return redirect('/')
    category_list = Category.objects.all().filter(user_id=request.user.id)
    return render(request, 'post/create.html', context={'category_list':category_list})


@require_POST
def store(request):
    if not request.user.is_authenticated:
        return redirect('/')
    post = Post()
    post.user_id = request.user.id
    post.category_id = request.POST['category']
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('/')
