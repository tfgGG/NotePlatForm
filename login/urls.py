from django.urls import re_path
from .import views

app_name = 'login'
urlpatterns = [
    re_path(r'^index/$', views.index, name="index"),#login homepage
    re_path(r'^register/$', views.UserFormView.as_view(), name="register"),
    re_path(r'^login/$', views.LoginFormView.as_view(), name="login"),
    re_path(r'^logout/$', views.logout_view, name="logout"),
    re_path(r'^now/$', views.now, name="now"),
]
