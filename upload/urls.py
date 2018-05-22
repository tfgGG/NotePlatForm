from django.urls import re_path,path
from .import views

app_name = 'upload'
urlpatterns = [
    #re_path(r'^main/$', views.main, name="main"),#login homepage
    re_path(r'^index/$', views.index, name="index"),
    path('detail/<int:note_id>/',views.detail, name="detail"),
    path('main/<int:note_id>/',views.main, name="main"),
]
