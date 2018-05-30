from django.shortcuts import render,redirect
from django.template import loader
from .models import Note,NoteList
from django.core import serializers
from django.contrib.auth import authenticate
from .form import NoteListForm,BaseNoteFormSet,PhotoForm
from django.views.generic import View
from django.forms import formset_factory,BaseFormSet
from django.contrib import messages
from django.db import IntegrityError,transaction

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

from PIL import Image

from django.conf import settings

def index(request):
    html = "hahah"
    note = Note.objects.all();
    #Sort/Search algorithm #
    return render(request,'upload/index.html',{"note":note})

# TODO: Detail Page will contain comment in the future
def detail(request,note_id):
    # TODO: Change to RESTFUL in the future
    notelist= NoteList.objects.filter(noteid = note_id).order_by("list_num")
    return render(request,'upload/detail_note.html',{"notelist":notelist,"noteid":note_id})


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

            except IntegrityError: #If the transaction failed
                messages.error(request, 'There was an error saving your ntoe.')
        else:
            messages.error(request, 'There was an error filed.')
    # end of if


    notelist = NoteList.objects.filter(noteid = note_id ).order_by('list_text')
    link_data = [{'list_text': l.list_text, 'note': l.note}
                    for l in notelist]
    note_formset = NoteFormSet(initial=link_data)

    photoform = PhotoForm()
    context = {
        'note_formset': note_formset,
        'photoform':photoform
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

        unit = Note.objects.create(field=field, subjects=subjects,textbook=textbook
        ,intro=intro,permission=permission,idnote=num,
        user_id=request.user.id,title=title)
        unit.save()
        return redirect('upload/index/')
    else:
        message = '請輸入資料(資料不作驗證)'
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
            resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
            resized_image.save(settings.BASE_DIR+"\\media\\crop"+ file[28:len(file)],"JPEG")

            data = {'file': "success"}

        return JsonResponse(data,safe=False);
