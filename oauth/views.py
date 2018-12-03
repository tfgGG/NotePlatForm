from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider import models
from django.http import HttpResponse,JsonResponse
from django.views import View
from login.models import User
from login.serializers import UserSerializer
from oauth2_provider import models

import json
#@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        temp = request.META['HTTP_AUTHORIZATION'].split(' ')
        instance = models.AccessToken.objects.filter(token = temp[1])
        user = 0
        for i in instance:
            user = i.user_id
            
        print(user)
        p = UserSerializer(User.objects.filter(id = user),many=True)
       
        return JsonResponse(p.data, safe=False)