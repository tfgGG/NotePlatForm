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
from person.models import User,Group,Groupuser
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
    #group = Group.objects.all()
    user = User.objects.all()
    group = Group.objects.filter(groupuser__userid = request.user.id)

    if request.path == "/person/Myfavorite/":
        note = Note.objects.filter(favorite__user= request.user)
    else:
        note = Note.objects.filter(user_id = request.user.id)

    json_data = open(settings.DATA_PATH,encoding = 'utf8')
    field = json.load(json_data)
    json_data.close()

    return render(request,'person/index.html',{"note":note,"field":field['field'] ,"group":group,"user":user})

def profile(request):
    if request.method == 'GET':
        profile = Profile.objects.filter(user_id = request.user.id)
        serializer = SnippetSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = request.FILES.get('img')
        unit = AuthUser.objects.filter(id=request.user.id)
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        unit.update(first_name=img)
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
        return redirect('../Team/'+str(unit.idgroup)+'/')

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
        return render(request,'person/Calender.html',{"plandetail":planteamdetail})
