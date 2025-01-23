from django.contrib import admin
from .models import Post, Category

# Post 모델을 관리 사이트에 등록
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'message', 'category', 'image', 'created_at', 'updated_at')  # 목록에서 어떤 필드를 보여줄지 설정
    search_fields = ('author_username', 'title', 'message',)  # 검색할 필드 설정
    list_filter = ('created_at', 'author', 'category')  # 필터링할 수 있는 필드 설정
    ordering = ('category', '-created_at',)  # 기본 정렬 기준 설정

# Tag 모델을 관리 사이트에 등록
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # 목록에서 보여줄 필드 설정
    search_fields = ('name',)  # 검색할 필드 설정

