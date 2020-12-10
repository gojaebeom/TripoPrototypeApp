from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

@require_GET
def main(request):
    return render(request, 'home.html')