from django.urls import re_path,path
from django.conf.urls.static import static
from .import views
from django.conf import settings
app_name = 'person'
urlpatterns = [
    re_path(r'^index/$', views.index, name="index"),
#    path('note/',views.note, name="note"),
    path('profile/',views.profile, name="profile"),
    path('upload/',views.uploadImg, name="upload"),
    path('Group/<int:userid>/',views.group, name="upload"),
    path('chat/<int:groupid>',views.chat, name="upload"),
    #path('Plan/<int:groupid>/',views.plan, name="upload"),
    path('Myfavorite/',views.index, name="Myfavorite"),
    path('CreateGroup/',views.CreateGroup,name="CreateGroup"),
    path('AddPlandetail/<int:teamid>/',views.AddPlandetail,name="AddPlandetail"),
    path('AddPlan/<int:teamid>',views.AddPlan,name="AddPlan"),
    path('AddMember/<int:teamid>',views.AddMember,name="AddMember"),
    path('MinusMember/<int:teamid>',views.MinusMember,name="MinusMember"),
    path('Team/Calender/<int:teamid>/',views.Team,name="Team"),
    path('Team/Planner/<int:teamid>/',views.Team,name="Plan"),
    path('Team/Note/<int:teamid>/',views.Team,name="GroupNote"),
    path('Team/Message/<int:teamid>/',views.Team,name="Plan"),
    path('Team/Member/<int:teamid>/',views.Team,name="Member"),
    path('deletePlandetail/',views.deletePlandetail,name="deletePlandetail"),
    path('deletePlan/',views.deletePlan,name="deletePlan"),
    #path('updatePlandetail/',views.updatePlandetail,name="updatePlandetail")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
