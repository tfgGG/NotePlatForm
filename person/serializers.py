from rest_framework import serializers
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from person.models import Group

class GroupRest(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
