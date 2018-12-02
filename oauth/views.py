from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider import models
from django.http import HttpResponse
from login.models import Profile
from oauth2_provider import models

#@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        temp = request.META['HTTP_AUTHORIZATION'].split(' ')
        instance = models.AccessToken.objects.filter(token = temp[1])
        for i in instance:
            u = i.user_id
        return redirect('http://localhost:3000/api/'+str(u))
