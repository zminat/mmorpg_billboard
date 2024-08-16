"""
URL configuration for mmorpg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mmorpg.views import upload_file

urlpatterns = (([
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('image_upload/', upload_file, name="ck_editor_5_upload_file"),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('ads/', include('billboard.urls')),
    path('', lambda request: redirect('ads/', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
