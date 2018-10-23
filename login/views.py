from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.views.generic import View
from django.views.generic.edit import CreateView
from .form import UserForm,LoginForm,AuthForm
from django.contrib.auth.models import User

from django.http import HttpResponse
from .models import Pet,Profile
from django.template import loader
from django.contrib import messages

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from login.serializers import SnippetSerializer
# Create your views here.
#from django.vierws import generic
#from .models import pet

def index(request):

    if not request.user.is_authenticated:
        return redirect('/login/login/')

    profile = Profile.objects.filter(user_id = request.user.id)
    context ={
        "profile":profile,
    }
    return render(request, 'login/index.html', context)

def now(request):
    if request.method == 'GET':
        profile = Profile.objects.filter(user_id = request.user.id)
        serializer = SnippetSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

#Create a Account
class UserFormView(View):
    template_name = 'login/regist_form.html'

    def get(self,request):
        user_form = AuthForm(None)
        profile_form = UserForm(None)
        return render(request,self.template_name,{'user_form': user_form,'profile_form': profile_form})

    def post(self,request):
        user_form = AuthForm(request.POST)
        profile_form = UserForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data.get('password'))
            user.save()
            profile = profile_form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = user.id
            profile.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect("/login/login/")
        else:
            messages.error(request, ('Please correct the error below.'))

        return render(request,self.template_name,{'user_form': user_form,'profile_form': profile_form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'login/login_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form': form })

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if not user or not user.is_active:
                messages.error(request, ('Please Enter valid password and username'))
            else:
                login(request,user)
                return redirect('/login/index/')
        else:
            messages.error(request, ('Form not valid'))
        return render(request,self.template_name, {'form': form })

def logout_view(request):
    logout(request)
    return redirect('/login/login/')
