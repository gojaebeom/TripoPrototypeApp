from typing import ContextManager
from post.models import Post
from django.shortcuts import redirect, render
from category.models import Category
from django.views.decorators.http import require_GET, require_POST

# 포스트 리스트 페이지 요청
@require_GET
def index(request):
    post_list = Post.objects.all()
    return render(request, 'post/index.html', {'post_list':post_list})


# 포스트 상세보기 페이지 요청
@require_GET
def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/show.html', {'post':post})


# 포스트 생성 페이지 요청
@require_GET
def create(request):
    # 로그인시에만 허가 되는 요청, 로그인 되지 않았다면 로그인 페이지로 이동 🍰
    if not request.user.is_authenticated:
        return redirect('/login-menu')

    category_list = Category.objects.all().filter(user_id=request.user.id)
    
    return render(request, 'post/create.html', context={'category_list':category_list})


# 포스트 생성 요청
@require_POST
def store(request):
    # 로그인시에만 허가 되는 요청, 로그인 되지 않았다면 로그인 페이지로 이동 🍰
    if not request.user.is_authenticated:
        return redirect('/')

    post = Post()
    post.user_id = request.user.id
    post.category_id = request.POST['category']
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()

    return redirect('/')
