from rest_framework import serializers
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from login.models import Profile

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
