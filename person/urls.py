from django.urls import re_path,path
from .import views

app_name = 'person'
urlpatterns = [
    re_path(r'^index/$', views.index, name="index"),
    path('note/',views.note, name="note"),
    path('profile/',views.profile, name="profile"),
]
