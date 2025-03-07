from django.urls import path
from . import views

app_name = 'user'

urlpatterns=[
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    path("change_password/", views.change_password, name="change_password"),
    path("user_profile/", views.user_profile, name="user_profile"),
]