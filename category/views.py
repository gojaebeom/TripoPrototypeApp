from django.shortcuts import render, redirect
from .models import Category
from django.views.decorators.http import require_GET, require_POST

# 카테고리 생성 페이지 요청
@require_GET
def create(request):
    # 이전 요청에 대한 URL을 할당
    prev_url = request.META.get('HTTP_REFERER')

    return_result = False
    if prev_url == 'http://127.0.0.1:8000/posts/create':
        print('포스트를 작성하려고 했던 유저입니다.')
        return_result = True
    return render(request, 'category/create.html',{'return_result':return_result})


# 카테고리 생성 요청
@require_POST
def store(request):
    category = Category()
    category.name = request.POST['name']
    category.user_id = request.user.id
    category.save()

    # 게시물을 생성하려고 했던 유저는 return_result가 True 값
    # 다시 포스트 생성 페이지로 이동시킨다.
    if request.POST['return_result'] == 'True':
        return redirect('/posts/create')\

    return redirect('/')