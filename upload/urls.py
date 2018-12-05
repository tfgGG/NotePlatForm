from django.urls import re_path,path
from . import views

app_name = 'upload'
urlpatterns = [
    #re_path(r'^main/$', views.main, name="main"),#login homepage
    re_path(r'^index/$', views.index, name="index"),
    path('detail/<int:note_id>/',views.detail, name="detail"),                      #Show the detail
    path('note/<int:note_id>/',views.note, name="note"),                      #GET note
    #path('create/',views.create, name="create"),
    path('ajaxpic/',views.ajaxpic, name="ajaxpic"),
    #path('change/',views.change, name="ajaxpic"),
    path('cropphoto/',views.cropphoto, name="cropphoto"),
    path('create/',views.create, name="create"),   
    path('POST/groupnote/',views.groupnote, name="groupnote"),                                    #POST create note
    #path('update/index2/',views.snippet_list, name="note"),
    #path('ajaxpic/',views.ajaxpic, name="ajaxpic"),
    path('GET/notedrop/',views.getnotedrop,name="getnotedrop"),
    path('comment/<int:note_id>/',views.comment, name="comment"),
    path('addComment/',views.addComment, name="addcomment"),
    path('addnotedetail/',views.DetailList.as_view()),
    path('putdetail/<int:id>/<int:num>',views.DetailPut),
    path('addLike/',views.addLike, name="addLike"),
    path('deleteNote/',views.deleteNote, name="addLike"),                           #刪除筆記
    path('RESTdetail/<int:note_id>/',views.RESTdetail, name="RESTdetail"),
    #path('refresh/<int:note_id>/',views.refresh, name="refresh"),

]
