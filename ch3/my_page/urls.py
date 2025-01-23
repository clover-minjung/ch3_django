"""
URL configuration for my_page project.

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
from django.urls import path

from django.urls.conf import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # (이 경로(주소)에 가서, 이 페이지(기능) 보여줘)
    path("admin/", admin.site.urls),

    # 각 앱의 urls를 분리해서 관리하고 싶음 (독립적) 
    # include = "각 앱에 관련된 모든 주소나 기능 등은 경로가 관리할 거니까 앱.urls를 확인해" 의미
    path("user/", include("user.urls")),
    path("", include("post.urls")),
]

# 사진 추가를 위한 설정
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)