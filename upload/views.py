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
from upload.models import Note,Message
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse,HttpResponseRedirect


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from snippets.models import Snippet
from upload.serializers import noteRest,CommentRESTAPI,detailRest
# Create your views here.

from django.core.files.storage import FileSystemStorage

#from PIL import Image
import redis
import hashlib


from django.conf import settings

note_url = "http://localhost:3000/"

def index(request):
    html = "hahah"
    note = Note.objects.all()
    #Sort/Search algorithm #
    return render(request,'upload/index.html',{"note":note})

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


def edit(request,note_id):

    NoteFormSet = formset_factory(NoteListForm, formset=BaseNoteFormSet)

    if request.method == 'POST':
        note_formset = NoteFormSet(request.POST)

        if note_formset.is_valid():
            print(note_formset.errors)
            note_list = []
            i= 1
            for link_form in note_formset:
                list_text = link_form.cleaned_data.get('list_text')
                note = link_form.cleaned_data.get('note')

                if list_text and note:
                    note_list.append(NoteList(noteid=note_id, note=note, list_text=list_text,list_num=i))
                else:
                    messages.error(request, 'Cannot be null')
                i=i+1

            try:
                with transaction.atomic():
                    #Replace the old with the new
                    NoteList.objects.filter(noteid = note_id).delete()
                    NoteList.objects.bulk_create(note_list)

                    # And notify our users that it worked
                    messages.success(request, 'You have updated your note.')

            except IntegrityError as e: #If the transaction failed
                messages.error(request, 'There was an error saving your ntoe.')
                print("!!!!IntegrityError!!!!"+ e)
        else:
            messages.error(request, 'There was an error filed.')
            for dict in note_formset.errors:
                for errors in dict:
                    print("!!!Form not Valid!!!"+ dict)
    # end of if


    notelist = NoteList.objects.filter(noteid = note_id ).order_by('list_text')
    link_data = [{'list_text': l.list_text, 'note': l.note}
                    for l in notelist]
    note_formset = NoteFormSet(initial=link_data)

    return render(request, "upload/edit_note.html", context = {'note_formset': note_formset,})



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
            # convert note id into 8 digit hash num
            hashnum = int(hashlib.sha256(str(lastid).encode("utf-8")).hexdigest(), 16) % (10 ** 8)
            return HttpResponseRedirect(note_url+'note/'+ str(hashnum))
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
