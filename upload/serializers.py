from rest_framework import serializers
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from upload.models import Note

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('idnote', 'user', 'title', 'field', 'subjects', 'textbook' , 'intro' , 'permission')
