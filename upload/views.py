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
from django.http import JsonResponse


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from snippets.models import Snippet
from upload.serializers import noteRest,CommentRESTAPI,detailRest
# Create your views here.


def index(request):
    html = "hahah"
    note = Note.objects.all();
    #Sort/Search algorithm #
    return render(request,'upload/index.html',{
        "note":note,
    })
#Detail Page will contain comment in the future
'''
def detail(request,note_id):
    # TODO: Change to RESTFUL in the future
    notelist= NoteList.objects.filter(noteid = note_id).order_by("list_num")


    #if request.method == "POST":
    #    message = request.POST['message']
    #    num=(UploadMessage2.objects.all().count()) + 1
    #    unit = UploadMessage2.objects.create(id=num,note_id=note_id
    #    ,message=message,user_id=request.user.id)
    #    unit.save()
    #    return redirect('http://127.0.0.1:8000/upload/index/')


    return render(request,'upload/detail_note.html',{"notelist":notelist,"noteid":note_id})
'''
def detail(request,note_id):
    if request.method == 'GET':
        notelist= NoteList.objects.filter(noteid = note_id).order_by("list_num")
        notelistRest = detailRest(notelist, many=True)
        return JsonResponse(notelistRest.data, safe=False)
#'''

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
'''
def refresh(request):
    #message = Message.objects.all()
    if request.method == "POST":
        message = request.POST[mes]

        num=(Message.objects.all().count()) + 1
        unit = Message.objects.create(id=num,note_id=note_id
        ,message=message)
        unit.save()

        return JsonResponse( "{ message : "+ " ' "+ message + " ' " + "}" )
'''
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

def create(request):
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
            'user' : request.user.id,
            'title'  : title,
            'field'  : field,
            'subjects': subjects,
            'textbook': textbook,
            'intro'  : intro,
            'permission': permission
        }
        unit = noteRest(data=data)
        if unit.is_valid():
            unit.save()
            return JsonResponse(unit.data, status=201)
        return JsonResponse(unit.errors, status=400)
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
        serializer = noteRest(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


'''
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

'''

def update(request,note_id):
    if request.method == 'GET':
        note_list = Note.objects.filter(idnote=note_id)
        note_listRest = noteRest(note_list, many=True)
        return JsonResponse(note_listRest.data, safe=False)
