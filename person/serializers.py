from rest_framework import serializers
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from person.models import Group,Plan

class GroupRest(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class PlanRest(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'