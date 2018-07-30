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
from upload.models import Note,Message
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import time,os
from selenium import webdriver

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from snippets.models import Snippet
from upload.serializers import SnippetSerializer
# Create your views here.


def index(request):
    html = "hahah"
    note = Note.objects.all();
    #Sort/Search algorithm #
    return render(request,'upload/index.html',{
        "note":note,
    })
#Detail Page will contain comment in the future
def detail(request,note_id):
    # TODO: Change to RESTFUL in the future
    notelist= NoteList.objects.filter(noteid = note_id).order_by("list_num")
    message = Message.objects.all()
    return render(request,'upload/detail_note.html',{"notelist":notelist,"noteid":note_id,"message":message})

def refresh(request):
    #message = Message.objects.all()
    if request.method == "POST":
        message = request.POST[mes]

        num=(Message.objects.all().count()) + 1
        unit = Message.objects.create(id=num,note_id=note_id
        ,message=message)
        unit.save()
        return JsonResponse( "{ message : "+ " ' "+ message + " ' " + "}" )




def ajaxpic(request):
    if request.method == 'POST':
        myfile = request.FILES.get("myfile")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print('Filename :'+ filename);
        uploaded_url = fs.url(filename)
        data = {"uploaded_url":uploaded_url}
        return JsonResponse(data)
    else:
        data={"uploaded_url":"There is some error occuring"}
        return JsonResponse(data)

    return JsonResponse(data)


def edit(request,note_id):

    # Create the formset, specifying the form and formset we want to use.
    NoteFormSet = formset_factory(NoteListForm, formset=BaseNoteFormSet)

    # Get our existing link data for this user.  This is used as initial data.

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

            except IntegrityError: #If the transaction failed
                messages.error(request, 'There was an error saving your ntoe.')
        else:
            messages.error(request, 'There was an error filed.')


    notelist = NoteList.objects.filter(noteid = note_id ).order_by('list_text')
    link_data = [{'list_text': l.list_text, 'note': l.note}
                    for l in notelist]
    note_formset = NoteFormSet(initial=link_data)

    context = {
        'note_formset': note_formset,
    }

    return render(request, "upload/edit_note.html", context)

def post(request):
    if request.method == "POST":
        title = request.POST['title']
        field = request.POST['field']
        subjects = request.POST['subjects']
        textbook = request.POST['textbook']
        intro = request.POST['introduction']
        permission = request.POST['permission']
        num=(Note.objects.all().count()) + 1

        mark = " ' "
        data = {
            'idnote' : num,
            'title'  : title,
            'field'  : field,
            'subjects': subjects,
            'textbook': textbook,
            'intro'  : intro,
            'permission': permission
        }
        unit = SnippetSerializer(data=data)
        if unit.is_valid():
            unit.save()
        return JsonResponse(unit.data, status=201)
        #return redirect('../index/')
    else:
        message = '請輸入資料(資料不作驗證)'
    return render(request,"upload/create_note.html",locals())
'''
def note(request):
    note_list = Note.objects.all()
    return render(request, 'upload/update.html', {
        'note_list': note_list,
    })
'''
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Note.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Note.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

def update(request,note_id):
    # TODO: Change to RESTFUL in the future
    note_list = Note.objects.get(idnote=note_id)
    if note_list.permission == 1 or note_list.user_id == request.user.id:
        if request.method == "POST":
            title = request.POST['title']
            field = request.POST['field']
            subjects = request.POST['subjects']
            textbook = request.POST['textbook']
            intro = request.POST['introduction']
            permission = request.POST['permission']
            unit = Note.objects.filter(idnote=note_id)
            unit.update(field=field, subjects=subjects,textbook=textbook
            ,intro=intro,permission=permission,
            title=title)
            return redirect('http://127.0.0.1:8000/upload/index/')
    else:
        return redirect('http://127.0.0.1:8000/upload/index/')

    return render(request,'upload/update.html',{
        'note_list': note_list,
    },locals())
