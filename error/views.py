from django.shortcuts import render

# Create your views here.
def res403(request):
    return render(request, 'error/403.html')