from django.urls import re_path,path
from .import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'person'
urlpatterns = [
    re_path(r'^index/$', views.index, name="index"),
#    path('note/',views.note, name="note"),
    path('profile/',views.profile, name="profile"),
    path('upload/',views.uploadImg, name="upload"),
    path('Myfavorite/',views.Myfavorite, name="Myfavorite"),
]
