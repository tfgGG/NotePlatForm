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
from person.models import Plandetail,Plan
#from NotePlatForm.models import AuthUser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from selenium import webdriver
from rest_framework.decorators import api_view
#from snippets.models import Snippet

from login.serializers import SnippetSerializer
from person.serializers import GroupRest,PlanRest,ChatRest
import json
# Create your views here.

def index(request):
    #group = Group.objects.all()
    user = User.objects.filter(~Q(id = request.user.id)) #除掉自己
    group = Group.objects.filter(groupuser__userid = request.user.id)

    if request.path == "/person/Myfavorite/":
        note = Note.objects.filter(favorite__user= request.user)
    else:
        note = Note.objects.filter(user_id = request.user.id).order_by('-idnote')

    json_data = open(settings.DATA_PATH,encoding = 'utf8')
    field = json.load(json_data)
    json_data.close()
    return render(request,'person/index.html',{"note":note,"subject":field['subject'] ,"group":group,"user":user})

def profile(request):
    if request.method == 'GET':
        profile = Profile.objects.filter(user_id = request.user.id)
        serializer = SnippetSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

def group(request,userid):
    if request.method == 'GET':
        group = Group.objects.filter(groupuser__userid = userid)
        serializer = GroupRest(group,many = True)
        return JsonResponse(serializer.data,safe=False)

def plan(requset,groupid):
    if request.method == 'GET':
        p = Plan.objects.filter(group = groupid)
        serializer = PlanRest(p,many = True)
        return JsonResponse(serializer.data,safe=False)

def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = request.FILES.get('img')
        unit = AuthUser.objects.filter(id=request.user.id)
        profileunit = Profile.objects.filter(user_id=request.user.id)
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        unit.update(first_name=img)
        profileunit.update(img=img)
    return render(request, 'person/uploadImg.html')


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
            id = User.objects.get(pk = m)
            memberunit = Groupuser.objects.create(userid= m ,group=unit)
            memberunit.save()
        return redirect('../Team/Calender/'+str(unit.idgroup)+'/')

def Team(request,teamid):
    if request.method == 'GET':
        user = Groupuser.objects.filter(group=teamid)
        Allnote = Note.objects.all()
        plan = Plan.objects.filter(groupid=teamid)
        planteamdetail = Plandetail.objects.filter(plan__groupid = teamid).order_by('plan')
        note = Note.objects.filter(plandetail__plan__groupid = teamid)
        group = Group.objects.filter(groupuser__userid = request.user.id)
        plancard = list(zip(planteamdetail,note))
        return render(request,'person/TeamIndex.html',{"plancard":plancard,
        "plan":plan,"teamid":teamid,"note":Allnote,"user":user,"group":group})

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
        assign = User.objects.get(pk = userid)
        plan = Plan.objects.get(pk = planid)
        unit = Plandetail.objects.create(note=note,assign=assign,start=start,end=end,plan=plan)
        unit.save()
        return redirect('/person/Team/Planner/'+str(teamid)+'/')

@api_view(['GET', 'POST'])
def chat(request,groupid):
    if request.method == 'POST':
        serializer = ChatRest(data=json.loads(request.body.decode('utf-8')))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)