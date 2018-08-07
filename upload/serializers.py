from rest_framework import serializers
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from upload.models import Note,UploadMessage2,NoteList

class noteRest(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class CommentRESTAPI(serializers.ModelSerializer):
    class Meta:
        model = UploadMessage2
        fields = '__all__'

class detailRest(serializers.ModelSerializer):
    class Meta:
        model = NoteList
        fields = '__all__'
