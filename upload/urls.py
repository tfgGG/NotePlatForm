from django.urls import re_path,path
from . import views

app_name = 'upload'
urlpatterns = [
    #re_path(r'^main/$', views.main, name="main"),#login homepage
    re_path(r'^index/$', views.index, name="index"),
    path('detail/<int:note_id>/',views.detail, name="detail"),                      #Show the detail
    path('update/<int:note_id>/',views.update, name="update"),                      #GET note
    #path('create/',views.create, name="create"),
    path('ajaxpic/',views.ajaxpic, name="ajaxpic"),
    path('cropphoto/',views.cropphoto, name="cropphoto"),
    path('create/',views.create, name="create"),                                    #POST create note
    #path('update/index2/',views.snippet_list, name="note"),
    #path('ajaxpic/',views.ajaxpic, name="ajaxpic"),
    path('Comment/<int:note_id>/',views.comment, name="comment"),
    path('addComment/<int:note_id>/',views.addComment, name="addcomment"),
    path('addnotedetail/',views.noteDetailList, name="note"),
    path('addLike/',views.addLike, name="addLike"),
    path('deleteNote/',views.deleteNote, name="addLike"),                           #刪除筆記
    path('RESTdetail/<int:note_id>/',views.RESTdetail, name="RESTdetail"),
    #path('refresh/<int:note_id>/',views.refresh, name="refresh"),

]
