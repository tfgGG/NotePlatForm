from django.shortcuts import render,redirect
from django.template import loader
from django.conf import settings
from django.db.models import Q
#from .models import Note,NoteList,UploadMessage2

from django.core import serializers
from django.contrib.auth import authenticate
#from .form import NoteListForm,BaseNoteFormSet
from django.views.generic import View
from django.contrib import messages
from django.db import IntegrityError,transaction
from upload.models import Note,Favorite
from login.models import Profile
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from person.models import User,Group,Groupuser
from person.models import Plandetail,Plan,Groupnote,Chat
#from NotePlatForm.models import AuthUser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from selenium import webdriver

from rest_framework.decorators import api_view
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

#from snippets.models import Snippet
from oauth2_provider import models
#from oauth2_provider.models import AbstractApplication

from login.serializers import SnippetSerializer
from person.serializers import GroupRest
import json
# Create your views here.

def index(request):
    #group = Group.objects.all()
    user = User.objects.filter(~Q(id = request.user.id)) #除掉自己
    group = Group.objects.filter(groupuser__userid = request.user.id)
    array =[]
    fav = Note.objects.filter(favorite__user_id = request.user.id).values('idnote')
    for f in fav:
        array.append(f['idnote'])



    if request.path == "/person/Myfavorite/":
        note = Note.objects.filter(favorite__user= request.user)
    else:
        note = Note.objects.filter(user_id = request.user.id)

    json_data = open(settings.DATA_PATH,encoding = 'utf8')
    field = json.load(json_data)
    json_data.close()
    return render(request,'person/index.html',{"note":note,"subject":field['subject']
                ,"group":group,"user":user,"fav":array})

def profile(request):
    if request.method == 'GET':
        #print(request.META['HTTP_REFERER'])
        #t  =request.META.get('HTTP_AUTHORIZATION')[:6:-1]
        o = models.get_application_model()
        g = o.objects.filter(client_id = 'gJzg99w4Trm42aN6R9GZbG9cyCxChnSMOehQw5sn').values_list('user_id',flat=True)
        #a = AbstractApplication.serializable_value(client_id = 'gJzg99w4Trm42aN6R9GZbG9cyCxChnSMOehQw5sn' )
        #print(type(g))
        #print(g[0])
        profile = Profile.objects.filter(user_id = g[0])
        serializer = SnippetSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

'''
class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = Profile.objects.filter(user_id = request.user.id)
    serializer_class = SnippetSerializer
'''

def group(request,userid):
    if request.method == 'GET':
        group = Group.objects.filter(groupuser__userid = userid)
        serializer = GroupRest(group,many = True)
        return JsonResponse(serializer.data,safe=False)


def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = request.FILES.get('img')
        unit = User.objects.filter(id=request.user.id)
        profileunit = Profile.objects.filter(user_id=request.user.id)
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        unit.update(first_name=img)
        profileunit.update(img=img)
        return redirect('/person/index/')

def CreateGroup(request):

    if request.method == 'POST':
        name = request.POST['groupName']
        createuser = User.objects.get(pk = request.user.id)
        unit = Group.objects.create(name=name, creator=createuser)
        unit.save()
        memberid = request.POST['tags']
        print(memberid)
        member = memberid.split(",")
        member.append(request.user.id)
        for m in member:
            print("flag")
            id = User.objects.get(pk = m)
            print(id)
            memberunit = Groupuser.objects.create(userid= id ,group=unit)
            memberunit.save()
        return redirect('../Team/'+str(unit.idgroup)+'/')

def Team(request,teamid):
    if request.method == 'GET':
        teamuser = Groupuser.objects.filter(group=teamid)
        user = User.objects.filter(~Q(id = request.user.id))
        Allnote = Note.objects.filter(permission=2)
        Allnote |= Note.objects.filter(user_id=request.user.id)
        plan = Plan.objects.filter(groupid=teamid)
        planteamdetail = Plandetail.objects.filter(plan__groupid = teamid).order_by('plan')
        note = Note.objects.filter(plandetail__plan__groupid = teamid)
        group = Group.objects.filter(groupuser__userid = request.user.id)
        plancard = list(zip(planteamdetail,note))

        json_data = open(settings.DATA_PATH,encoding = 'utf8')
        field = json.load(json_data)
        json_data.close()
        
        GroupNote = Note.objects.none()
        GN = Note.objects.all()
        for n in GN:
            if n.permission.isdigit() == 0:
                gp = n.permission.split(' ')
                print(gp)
                if gp[1] == str(teamid):
                    GroupNote |= Note.objects.filter(permission=n.permission)
        GPN = Groupnote.objects.filter(group=teamid)
        for n in GPN:
            if str(n.group.idgroup) == str(teamid):
                GroupNote |= Note.objects.filter(groupnote__note=n.note)
        return render(request,'person/TeamIndex.html',{"plancard":plancard,
        "plan":plan,"teamid":teamid,"Allnote":Allnote,"user":user,"teamuser":teamuser,"group":group,
        "subject":field['subject'],"note":GroupNote,"GPN":GPN })

def AddPlan(request,teamid):
    if request.method == 'POST':
        planName = request.POST['planName']
        tid = Group.objects.get(pk = teamid)
        unit = Plan.objects.create(name=planName,groupid=tid)
        unit.save()
        return redirect('../Team/Planner/'+str(teamid)+'/')

def AddPlandetail(request,teamid):
    if request.method == 'POST':
        noteid = request.POST['noteid']
        userid = request.POST['user']
        planid = request.POST['plan']
        start = request.POST['startDate']
        end = request.POST['endDate']
        note = Note.objects.get(pk = noteid)
        print(userid)
        assign = User.objects.get(username = userid)
        plan = Plan.objects.get(pk = planid)
        unit = Plandetail.objects.create(note=note,assign=assign,start=start,end=end,plan=plan)
        unit.save()
        return redirect('/person/Team/Planner/'+str(teamid)+'/')

@csrf_exempt
def chat(request,groupid):
    if request.method == 'POST':
        print("CHAT POST")
        print(json.loads(request.body.decode('utf-8')))
        serializer = ChatRest(data=json.loads(request.body.decode('utf-8')))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
         chat = Chat.objects.filter(teamid = groupid)


@csrf_exempt
def deletePlandetail(request):
    if request.method == 'POST':
        planid = request.POST.get('id',None)
        print(planid)
        plandetail = Plandetail.objects.get(idplandetail = planid)
        plandetail.delete()
        return HttpResponse(0)


@csrf_exempt
def deletePlan(request):
    if request.method == 'POST':
        planid = request.POST.get('idplan',None)
        print(planid)
        plandetail = Plandetail.objects.filter(plan = planid)
        plandetail.delete()
        plan = Plan.objects.get(idplan = planid)
        plan.delete()
        return HttpResponse(0)

def GroupNote(request,teamid):
    if request.method == 'GET':
        note = Note.objects.all()

