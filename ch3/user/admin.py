from django.contrib import admin
from .models import CustomUser  # CustomUser 가져오기

@admin.register(CustomUser)  # CustomUser 모델 관리자에 등록하기
class CustomUserAdmin(admin.ModelAdmin):
    # 사용자 관리에서 어떤 필드를 보일지 설정합니다.
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')  # 표에 보일 필드
    list_filter = ('is_active', 'is_staff', 'is_superuser')  # 필터 옵션
    search_fields = ('username', 'email')  # 검색 가능한 필드
    ordering = ('username',)  # 기본 정렬 기준

    # 프로필 이미지와 다른 필드를 관리자 화면에서 수정할 수 있도록 필드 추가
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_image')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Profile Info', {
            'fields': ('profile',)  # Profile 객체와 연관된 필드
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )

    filter_horizontal = ('groups', 'user_permissions')  # 그룹 및 사용자 권한 필터링을 추가할 경우 사용
