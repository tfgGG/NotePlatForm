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
            return self.errors

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
