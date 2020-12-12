"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import config.views
import panorama.views
import customuser.views


urlpatterns = [
    # DJANGO DEFAULT URL 🧀
    # GET /admin/
    path('admin/', admin.site.urls), 

    # MAIN URL
    # GET /
    path('', config.views.main), 

    # PANORAMA URL 🧀
    # GET /panorama
    path('panorama/', panorama.views.index),
    # GET /panorama/:id
    path('panorama/<int:id>', panorama.views.show),
    # GET /panorama/create
    path('panorama/create', panorama.views.create),
    # POST /panorama/store
    path('panorama/store', panorama.views.store),
    # GET /panorama/:id/update
    path('panorama/<int:id>/update', panorama.views.update),
    # POST /panorama/:id/edit
    path('panorama/<int:id>/edit', panorama.views.edit),
    # GET /panorama/:id/destroy
    path('panorama/<int:id>/destroy', panorama.views.destroy),

    # SIGN URL 🧀
    # GET or POST /login
    path('login/', customuser.views.login),
    # GET or POST /join
    path('join/', customuser.views.join),
    # GET /login-menu
    path('login-menu/', customuser.views.login_menu),
    # GET /logout
    path('logout/', customuser.views.logout),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
