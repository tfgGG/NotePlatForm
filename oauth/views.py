from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

#@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        print(request.user.id)
        return HttpResponse('Hello, OAuth2!')