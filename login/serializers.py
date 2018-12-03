from rest_framework import serializers
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from login.models import Profile,User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','email','username']