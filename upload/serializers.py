from rest_framework import serializers
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from upload.models import Note,Message,NoteList
from person.models import Groupnote

class noteRest(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class CommentRESTAPI(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class detailRest(serializers.ModelSerializer):
    class Meta:
        model = NoteList
        fields = '__all__'

class GroupnoteRest(serializers.ModelSerializer):
    class Meta:
        model = Groupnote
        fields = '__all__'
