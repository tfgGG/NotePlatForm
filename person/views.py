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
from person.models import AuthUser
#from NotePlatForm.models import AuthUser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from snippets.models import Snippet

from login.serializers import SnippetSerializer
from login.models import Profile
import json
# Create your views here.

def index(request):
    PersonNote = Note.objects.filter(user_id = request.user.id)
    json_data = open(settings.DATA_PATH,encoding = 'utf8')
    field = json.load(json_data)
    json_data.close()
    return render(request,'person/index.html',{"note":PersonNote,"field":field['field']})

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

def Myfavorite(request):
    note = Note.objects.filter(favorite__user= request.user)
    return render(request,'person/index.html',{"note":note })
