from django.shortcuts import render, redirect
from .models import Category
from django.views.decorators.http import require_GET, require_POST

# Create your views here.
@require_GET
def create(request):
    return render(request, 'category/create.html')

@require_POST
def store(request):
    category = Category()
    category.name = request.POST['name']
    category.user_id = request.user.id
    category.save()
    return redirect('/')