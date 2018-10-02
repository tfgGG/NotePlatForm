from django.shortcuts import render,redirect
from django.template import loader
#from .models import Note,NoteList,UploadMessage2
from django.core import serializers
from django.contrib.auth import authenticate
#from .form import NoteListForm,BaseNoteFormSet
from django.views.generic import View
from django.forms import formset_factory,BaseFormSet
from django.contrib import messages
from django.db import IntegrityError,transaction
from upload.models import Note,Message,NoteList
from login.models import Profile
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from snippets.models import Snippet
from upload.serializers import noteRest,CommentRESTAPI,detailRest
from login.serializers import SnippetSerializer
from login.models import Profile
# Create your views here.
def index(request):
    #Sort/Search algorithm #
    return render(request,'person/index.html')

def note(request):
    if request.method == 'GET':
        PersonNote = Note.objects.filter(user_id = request.user.id)
        PersonNoteRest = noteRest(PersonNote, many=True)
        return JsonResponse(PersonNoteRest.data, safe=False)

def profile(request):
    if request.method == 'GET':
        profile = Profile.objects.filter(user_id = request.user.id)
        serializer = SnippetSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = request.FILES.get('img')
        unit = Profile.objects.filter(user_id=request.user.id)
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        unit.update(img=img)
    return render(request, 'person/uploadImg.html')
