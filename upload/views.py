from django.shortcuts import render,redirect
from django.template import loader
from .models import Note,NoteList,Message
from django.core import serializers
from django.contrib.auth import authenticate
from .form import NoteListForm,BaseNoteFormSet
from django.views.generic import View
from django.forms import formset_factory,BaseFormSet
from django.contrib import messages
from django.db import IntegrityError,transaction
from django.db.models import Avg, Max, Min
from upload.models import Note,Message,Favorite
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse,HttpResponseRedirect
from person.models import Group, Groupuser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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

def dec(h):
    hashid = Hashids(min_length=6)
    hashnum = hashid.decode(h)
    print(hashnum)
    return hashnum
@csrf_exempt
def index(request):
    json_data = open(settings.DATA_PATH,encoding = 'utf8')
    field = json.load(json_data)

    array = []
    note = Note.objects.all().order_by('-idnote')
    fav = Note.objects.filter(favorite__user_id = request.user.id).values('idnote')
    for f in fav:
        array.append(f['idnote'])
    #Sort/Search algorithm #
    if request.method == 'POST':
        noteSearch = request.POST['searchNote']
        searchTags = request.POST['searchTags']
        note = Note.objects.none()
        if searchTags != '':
            noteTag = searchTags.split(",")
            for n in noteTag:
                tmp = Note.objects.filter(field__contains=n)
                if tmp:
                    note |= tmp
        elif noteSearch != '':
            note = Note.objects.filter(title__contains=noteSearch).order_by('-idnote')
        json_data.close()
        return render(request,'upload/index.html',{"note":note,"fav":array,"subject":field['subject']})#field改成subject

    json_data.close()
    return render(request,'upload/index.html',{"note":note,"fav":array,"subject":field['subject']})

@csrf_exempt
def addLike(request):
    if request.method == 'POST':

        idnote = request.POST.get('id')
        obj = Note.objects.get(pk=idnote)

        data= Note.objects.filter(favorite__user=request.user.id,pk=idnote)
        print("~~~Afeter Filt~~~~"+ str(data.count()))
        if(data):
            Favorite.objects.filter(user=request.user,idnote=obj).delete()
            return HttpResponse(0)
        else:
            print("Inside Else")
            unit = Favorite.objects.create(user=request.user,idnote=obj)
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
        comment = Message.objects.select_related('user').filter(note = note_id)
        commentRest = CommentRESTAPI(comment, many=True)
        print(commentRest)
        return JsonResponse(commentRest.data, safe=False)

@csrf_exempt
def addComment(request):
    if request.method == "POST":
        serializer = CommentRESTAPI(data=json.loads(request.body.decode('utf-8')))
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=400)


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

#新增筆記及第一項
def create(request):
    if request.method == "POST":
        title = request.POST['title']
        field = request.POST['field']
        subjects = request.POST['subjects']
        intro = request.POST['introduction']
        permission = request.POST['permission']
        group = request.POST['group']
        mark = " ' "
        data = {
            'user' : request.user.id,
            'title'  : title,
            'field'  : field,
            'subjects': subjects,
            'intro'  : intro,
            'permission': permission+' '+group
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
                hashnum2 = hash(lastid*100 + 1)
                print(lastdetailid)
                return HttpResponseRedirect(note_url+'/note/'+ str(hashnum)+'/'+ str(hashnum2))
        else:
            message = '請輸入資料(資料不作驗證)'
            return JsonResponse(unit.errors, status=400)
        #return redirect('../index/')
    if request.method == "GET":
        return render(request,"person/index.html",locals())

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

@csrf_exempt
def note(request,note_id):
    if request.method == 'GET':
        note_list = Note.objects.filter(idnote=note_id)
        note_listRest = noteRest(note_list, many=True)
        return JsonResponse(note_listRest.data, safe=False)


#新增及更新筆記細項

class DetailList(APIView):

    def post(self,request):
        serializer = detailRest(data=json.loads(request.body.decode('utf-8')))
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT','PATCH'])
def DetailPut(request,id,num):
    if request.method == 'PUT':
        notedetail = NoteList.objects.filter(noteid = id , list_num = num).first()
        data = json.loads(request.body.decode('utf-8'))
        #print(data)
        data['noteid'] = id
        data['idnote_list'] = notedetail.idnote_list
        serializer = detailRest(notedetail, data=data)
        if serializer.is_valid():
            serializer.save()
            #print(str(serializer.data))
            return Response(serializer.data)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        #print("Inside Patch"+ id +" "+num)
        notedetail = NoteList.objects.filter(noteid = id , list_num = num).first()
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        serializer = detailRest(notedetail, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#刪除筆記function
@csrf_exempt
def deleteNote(request):
    if request.method == 'POST':
        user_id = request.user.id
        idnote = request.POST.get('id',None)
        print(idnote)
        data_list = NoteList.objects.filter(noteid=idnote)
        data_list.delete()
        fav_note = Favorite.objects.filter(idnote=idnote)
        fav_note.delete()
        data= Note.objects.get(idnote=idnote)
        data.delete()
        return HttpResponse(0)
