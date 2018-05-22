from django.shortcuts import render,redirect
from django.template import loader
from .models import Note,NoteList
from django.core import serializers
from django.contrib.auth import authenticate
from .form import NoteListForm,BaseNoteFormSet
from django.views.generic import View
from django.forms import formset_factory,BaseFormSet
from django.contrib import messages
from django.db import IntegrityError,transaction
# Create your views here.


def index(request):
    html = "hahah"
    note = Note.objects.all();
    newindex =  1
    #Sort/Search algorithm #
    return render(request,'index.html',{"note":note,"newindex":newindex})

#Detail Page will contain comment in the future
def detail(request,note_id):
    # TODO: Change to RESTFUL in the future
    notelist= NoteList.objects.filter(noteid = note_id).order_by("list_num")

    return render(request,'detail_note.html',{"notelist":notelist,})

'''
class main(View):
    #model = Note
    #template_name = 'upload_note.html'
    #form_class = NoteListForm
    #note_id = 1

    def get_from_kwargs(self):
        kwargs = super(main, self).get_form_kwargs()
        kwargs.update({'note_id': self.note_id})
        return kwargs

    def get(self,request):
        #note = Note.objects.get(pk=self.note_id)
        note_form = NoteListForm()
        for field_name in note_form.fields:
            if field_name.startswith('note'):
                yield note_form[field_name]
        return render(request,"upload_note.html",{'note_form': note_form})
'''

'''
class main(View):

    def get(self,request):
        #note = Note.objects.get(pk=self.note_id)
        note_form = NoteListForm()
        return render(request,"uplaod_note.html",{'note_form': note_form})

    #def post(self,request):
    #    return render(request,"upload_note.html",{'note_form': note_form})

'''

def main(request,note_id):
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

    return render(request, "uplaod_note.html", context)
