from django.shortcuts import render,redirect
from django.template import loader
from .models import Note,NoteList,UploadMessage2
from django.core import serializers
from django.contrib.auth import authenticate
from .form import NoteListForm,BaseNoteFormSet
from django.views.generic import View
from django.forms import formset_factory,BaseFormSet
from django.contrib import messages
from django.db import IntegrityError,transaction
from upload.models import Note,Message,Favorite
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse,HttpResponseRedirect

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
#from snippets.models import Snippet
from upload.serializers import noteRest,CommentRESTAPI,detailRest
# Create your views here.

from django.core.files.storage import FileSystemStorage

#from PIL import Image
import redis
import json
from hashids import Hashids
hashids = Hashids()

from django.conf import settings

note_url = "http://localhost:3000"

def hash(num):
    #hashids = Hashids()
    hashid = Hashids(min_length=6)
    hashnum = hashid.encode(num)
    return hashnum

def index(request):
    array = []
    note = Note.objects.all()
    fav = Favorite.objects.filter(user_id=request.user.id).values("idnote")
    for favs in fav:
        print(favs)
        array.append(favs['idnote'])
    #Sort/Search algorithm #
    return render(request,'upload/index.html',{"note":note,"fav":array})

@csrf_exempt
def addLike(request):
    if request.method == 'POST':
        user_id = request.user.id
        idnote = request.POST.get('id',None)
        print(idnote)
        data= Favorite.objects.filter(user_id=user_id,idnote=idnote)
        if(data):
            data.delete()
            return HttpResponse(0)
        else:
            unit = Favorite.objects.create(user_id=user_id,idnote=idnote)
            unit.save()
            return HttpResponse(1)

# TODO: Detail Page will contain comment in the future
def detail(request,note_id):
    # TODO: Change to RESTFUL in the future
    notelist= NoteList.objects.filter(noteid = note_id).order_by("list_num")
    return render(request,'upload/detail_note.html',{"notelist":notelist,"noteid":note_id})

def RESTdetail(request,note_id):
    if request.method == 'GET':
        notelist= NoteList.objects.filter(noteid = note_id).order_by("list_num")
        notelistRest = detailRest(notelist, many=True)
        return JsonResponse(notelistRest.data, safe=False)

def comment(request,note_id):
    if request.method == 'GET':
        comment = UploadMessage2.objects.filter(note_id = note_id)
        commentRest = CommentRESTAPI(comment, many=True)
        return JsonResponse(commentRest.data, safe=False)

def addComment(request,note_id):
    if request.method == "POST":
        message = request.POST['message']
        num=(UploadMessage2.objects.all().count()) + 1
        data = {
            'id' : num,
            'note_id' : note_id,
            'message' : message,
            'user' : request.user.id,
        }
        mes = CommentRESTAPI(data=data)
        if mes.is_valid():
            mes.save()
            return JsonResponse(mes.data, status=201)
        return JsonResponse(mes.errors, status=400)
    return render(request,"upload/addComment.html",locals())

def ajaxpic(request):
    if request.method == 'POST':
        myfile = request.FILES.get("myfile")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print('Filename :'+ filename)
        uploaded_url = fs.url(filename)
        data = {"uploaded_url":uploaded_url}
        return JsonResponse(data)
    else:
        data={"uploaded_url":"There is some error occuring"}
        return JsonResponse(data)

    return JsonResponse(data)


def create(request):
    if request.method == "POST":
        title = request.POST['title']
        field = request.POST['field']
        subjects = request.POST['subjects']
        textbook = request.POST['textbook']
        intro = request.POST['introduction']
        permission = request.POST['permission']

        mark = " ' "
        data = {
            'user' : request.user.id,
            'title'  : title,
            'field'  : field,
            'subjects': subjects,
            'textbook': textbook,
            'intro'  : intro,
            'permission': permission
        }
        # Save to db via note rest
        unit = noteRest(data=data)
        if unit.is_valid():
            #create a new note with info
            unit.save()
            # get the note id just created
            lastid = Note.objects.last().idnote

            detaildata={
                "list_text":"Edit Here",
                "list_num":1,
                "noteid":lastid
            }
            unitdetail = detailRest(data = detaildata)
            if unitdetail.is_valid():
                unitdetail.save()
                lastdetailid = NoteList.objects.last().idnote_list
                hashnum = hash(lastid)
                hashnum2 = hash(lastdetailid)
                print(lastdetailid)
                return HttpResponseRedirect(note_url+'/note/'+ str(hashnum)+'/'+ str(hashnum2))
        else:
            message = '請輸入資料(資料不作驗證)'
            return JsonResponse(unit.errors, status=400)
        #return redirect('../index/')
    if request.method == "GET":
        return render(request,"upload/create_note.html",locals())

def cropphoto(request):

        if request.method == 'POST':
            x = int(request.POST.get('x'))
            y = int(request.POST.get('y'))
            width = int(request.POST.get('width'))
            height = int(request.POST.get('height'))
            file= request.POST.get('file')
            file = settings.BASE_DIR+"\\media\\" + file[28:len(file)]

            print(file)
            image = Image.open(file)
            cropped_image = image.crop((x, y, width+x, height+y))
            resized_image = cropped_image.resize((width, height), Image.ANTIALIAS)
            resized_image.save(settings.BASE_DIR+"\\media\\crop"+ file[28:len(file)],"JPEG")

            data = {'file': "success"}

        return JsonResponse(data,safe=False)

def update(request,note_id):
    if request.method == 'GET':
        note_list = Note.objects.filter(idnote=note_id)
        note_listRest = noteRest(note_list, many=True)
        return JsonResponse(note_listRest.data, safe=False)
'''
@csrf_exempt
def noteDetailList(request,note_id):
    if request.method == "POST":
        list_text = request.POST.get('list_text',None)
        note = request.POST.get('note',None)

        data = {
            "list_text": list_text,
            "list_num": list_num,
            "note" : note,
            "noteid": note_id
        }
        noteDetail = detailRest(data = data)
        if noteDetail.is_valid():
            noteDetail.save()
            return JsonResponse(noteDetail.data, status=201)
        return JsonResponse(noteDetail.errors, status=400)
    #if request.method == "GET":

    return render(request,"upload/noteDetail.html",locals())
'''
@csrf_exempt
@api_view(['GET', 'POST'])
def noteDetailList(request):
    if request.method == 'POST':
        serializer = detailRest(data=json.loads(request.body.decode('utf-8')))
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
