from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from django.core.exceptions import ValidationError
from .models import Note,NoteList
from django.forms import BaseFormSet
from django.forms import formset_factory

class NoteListForm(forms.ModelForm):

    class Meta:
        model= NoteList
        fields = ["list_text","note"]
        widgets = {'note': forms.HiddenInput()}

class BaseNoteFormSet(BaseFormSet):

    def clean(self):

        if any(self.errors):
            return

        list_text = []
        note = []

        for form in self.forms:
            if form.cleaned_data:
                text = form.cleaned_data['list_text']
                n = form.cleaned_data['note']

                # Check that no two links have the same list_text or URL

                if n is None:
                    raise forms.ValidationError("Note Null")
                else:
                    note.append(n)


                if text is None:
                    raise forms.ValidationError("text Null")
                else:
                    list_text.append(text)

        return self.cleaned_data







'''
class NoteListForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        notelist= NoteList.objects.filter(noteid = 1).order_by("list_num")
        j=0
        for n in notelist:
            field_name = "note_" + str(j)
            field_name2 = "list_text_" + str(j)
            self.fields[field_name] = forms.CharField()
            self.initial[field_name] = n.note
            self.fields[field_name2] = forms.CharField()
            self.initial[field_name2] = n.list_text
            j=j+1

    def clean(self):
        note_set = set()
        list_text_set= set()
        j=0
        field_name = "note_" + str(j)
        field_name2 = "list_text_" + str(j)
        while self.cleaned_data.get(field_name):
            note = self.cleaned_data[field_name]
            list_text = self.cleaned_data[field_name2]
            if note is None:
                raise forms.ValidatiErrors("Note Null"+ j)
            else:
                note_set.add(note)
            if list_text is None:
                raise forms.ValidatiErrors("list_text Null" + j)
            else:
                list_text_set.add(list_text)
            field_name = "note_" + str(j)
            field_name2 = "list_text_" + str(j)
            j=j+1

        self.cleaned_data["note_set"]= note_set
        self.cleaned_data['list_text']= list_text_set
        return self.cleaned_data

    def get_list_fields(self):
        for field_name in self.fields:
            if field_name.startswith("list_text_"):
                yield self[field_name]


    def save(self):
        NoteList.note_set.all().delete()
        i=0
        for n in self.cleaned_data['list_text_']:
            NoteList.objects.create(list_text=n, list_num=i, note=n, noteid= 1)
'''
