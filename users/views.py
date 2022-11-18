from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class UserLogin(LoginView):
    template_name = 'users/login.html'


def homepage_view(request):
    return render(request, 'users/index.html')

def userprofile_view(request):
    return render(request, 'users/profile.html')

def uploadblog_view(request):
    return render(request, 'users/upload.html')


class LogoutUser(LogoutView):
    template_name = 'users/logout.html'