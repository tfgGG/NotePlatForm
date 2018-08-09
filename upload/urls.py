from django.urls import re_path,path
from .import views

app_name = 'upload'
urlpatterns = [
    #re_path(r'^main/$', views.main, name="main"),#login homepage
    re_path(r'^index/$', views.index, name="index"),
    path('detail/<int:note_id>/',views.detail, name="detail"),
    path('update/<int:note_id>/',views.update, name="update"),
    path('edit/<int:note_id>/',views.edit, name="main"),
    path('post/',views.post, name="post"),
    path('ajaxpic/',views.ajaxpic, name="ajaxpic"),
    path('cropphoto/',views.cropphoto, name="cropphoto"),
    path('create/',views.create, name="create"),
    path('update/index2/',views.snippet_list, name="note"),
    path('ajaxpic/',views.ajaxpic, name="ajaxpic"),
    path('Comment/<int:note_id>/',views.comment, name="comment"),
    path('addComment/<int:note_id>/',views.addComment, name="comment"),
    #path('refresh/<int:note_id>/',views.refresh, name="refresh"),

]
