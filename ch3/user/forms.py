from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=10)
    message = forms.CharField()

# 장고 깃허브의 오픈 소스를 확인하면 쓸 수 있음
from .models import CustomUser  # 커스텀 사용자 모델 가져오기

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model#현재 활성화 되어서 쓰여지고 있는 유저 모델에 항상 접근 가능하게 하는 함수
from django.urls import reverse  


# 오버라이딩
# 코드 UserCreationForm -> BaseUserCreationForm 따라가기
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            'profile_image',
            'bio',
            "first_name",
            "last_name",
            "email",
            
        ]
    # UserChangeForm 까보기
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if self.fields.get("password"):
                password_help_text = (
                    '<a href="{}"><strong>여기</strong></a>'"를 누르면 비밀번호 변경 페이지로 이동합니다."
                ).format(f"{reverse('user:change_password')}")
                self.fields["password"].help_text = password_help_text