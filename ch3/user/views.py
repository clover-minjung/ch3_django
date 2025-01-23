from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required

from user.forms import CustomUserChangeForm, CustomUserCreationForm


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # 로그인 성공시 이전 페이지로 자동으로 이동
            next_path = request.GET.get("next") or "post:category_list"
            return redirect(next_path)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "user/login.html", context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("post:category_list")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입 후 기억해서 바로 로그인하기
            user = form.save()
            auth_login(request, user)
            return redirect("post:category_list")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "user/signup.html", context)

@require_POST
def delete(requset):
    if requset.user.is_authenticated:
        requset.user.delete()
        auth_logout(requset)
    return redirect("post:category_list")

@require_http_methods(["GET", "POST"])
def update(request):
    print(f"Request method: {request.method}")
    if request.method=="POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user:user_profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form' : form}
    return render(request, "user/update.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('post:category_list')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form' : form}
    return render(request, "user/change_password.html", context)

def user_profile(request):
    form = CustomUserChangeForm(instance=request.user)
    context = {'form' : form}
    return render(request, "user/user_profile.html", context)
    # return render(request, 'user/user_profile.html', {'user': request.user})
