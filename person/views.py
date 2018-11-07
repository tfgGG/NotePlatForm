from django.shortcuts import render,redirect
from django.template import loader
from django.conf import settings
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
from person.models import AuthUser,Group,Groupuser
from person.models import Plandetail,Plan
#from NotePlatForm.models import AuthUser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from snippets.models import Snippet

from login.serializers import SnippetSerializer
import json
# Create your views here.

def index(request):
    group = Group.objects.all()
    PersonNote = Note.objects.filter(user_id = request.user.id)
    json_data = open(settings.DATA_PATH,encoding = 'utf8')
    field = json.load(json_data)
    json_data.close()
    return render(request,'person/index.html',{"note":PersonNote,"subject":field['subject'] ,"group":group})

def profile(request):
    if request.method == 'GET':
        profile = Profile.objects.filter(user_id = request.user.id)
        serializer = SnippetSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

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

def Myfavorite(request):
    note = Note.objects.filter(favorite__user= request.user)
    return render(request,'person/index.html',{"note":note })
@csrf_exempt
def CreateGroup(request):
    user = AuthUser.objects.all()
    if request.method == 'POST':
        name = request.POST['groupName']
        unit = Group.objects.create(name=name, creator=request.user.id)
        unit.save()
        memberid = request.POST['tags']
        member = memberid.split(",")
        groupid=Group.objects.get(name=name)
        for member in member:
            id = AuthUser.objects.get(username=member).id
            memberunit = Groupuser.objects.create(userid=id,group=groupid.idgroup)
            memberunit.save()
        return redirect('../Team/'+str(groupid.idgroup)+'/')
    return render(request,'person/CreateGroup.html',{"user":user})

def Team(request,teamid):
    if request.method == 'GET':
        planteamdetail = Plandetail.objects.none()
        print(planteamdetail.values())
        plan = Plan.objects.filter(groupid=teamid)
        plandetail = Plandetail.objects.all()
        for p1 in plandetail:
            for p2 in plan:
                if str(p2.idplan) == str(p1.plan.idplan):
                    planteamdetail |= Plandetail.objects.filter(plan=p2.idplan)

        print(planteamdetail.values())
        #print(plandetail.start)
        return render(request,'person/Team.html',{"plandetail":planteamdetail})
