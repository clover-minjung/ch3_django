from django.urls.conf import path
from . import views

app_name = 'post'

urlpatterns=[
    # 카테고리 별 글 목록, 글 작성
    path(route="", view=views.category_list, name='category_list'),
    path(route='<int:category_id>/category_detail/', view=views.category_detail, name="category_detail"),
    path("category/none/", views.category_detail, {"category_id": None}, name="no_category_posts"),
    
    # 전체 글 목록, 글 작성, 조회, 수정, 삭제
    path(route='post_list/', view=views.post_list, name="post_list"),
    path(route='post_create/', view=views.post_create, name="post_create"),
    path(route='<int:pk>/', view=views.post_detail, name="post_detail"),
    path(route="<int:pk>/post_update/", view=views.post_update, name="post_update"),
    path(route="<int:pk>/post_delete/", view=views.post_delete, name="post_delete"),
]