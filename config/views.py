from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from post.models import Post

@require_GET
def main(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list':post_list})