import os

from django.http.response import HttpResponse
from panorama.models import PanoramaPost
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from PIL import Image
from uuid import uuid4
import json
from django.core import serializers

# Create your views here.
@require_GET
def index(request):
    pano_list = PanoramaPost.objects.all()
    return render(request, 'panorama/index.html', context={'pano_list': pano_list})


@require_GET
def show(request, id):
    print(id)
    pano = PanoramaPost.objects.get(id=id)
    print(pano)
    return render(request, 'panorama/show.html', context={'pano': pano})


@require_GET
def create(request):
    return render(request, 'panorama/create.html')


@require_POST
def store(request):
    print('PANORAMA STORE 요청 받음')
    title = request.POST.get('title')
    panorama_img = request.FILES.get('panorama')
    bgm = request.FILES.get('bgm')
    print(title)
    print(panorama_img)
    print(bgm)

    # 데이터베이스에 데이터 저장하는 부분
    # 확장자 추출
    extension = os.path.splitext(panorama_img.name)[-1].lower()
    # 이미지 원본 이름을 따로 받아둔다
    origin_name = panorama_img.name
    # 길이 32 인 uuid 값과 확장자명을 조합하여 중복되지 않는 이름으로 변경
    panorama_img.name = uuid4().hex + extension

    panorama_post = PanoramaPost()
    panorama_post.title = title
    panorama_post.image = panorama_img
    panorama_post.image_origin_name = origin_name
    if bgm :
        panorama_post.bgm = bgm
    panorama_post.save()

    return redirect('/panorama/')


@require_GET
def update(request):
    return render(request, 'panorama/update.html')


@require_POST
def edit(request):
    return redirect('/')


@require_GET
def destroy(request):
    return redirect('/')


def getBgm(request):
    data = json.loads(request.body)
    print(data)
    pano = PanoramaPost.objects.get(id=id)

    jsonfile = serializers.serialize('json', pano.bgm.url)

    return HttpResponse(jsonfile, content_type="application/json")