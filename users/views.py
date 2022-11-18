from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class UserLogin(LoginView):
    template_name = 'login.html'


def homepage_view(request):
    return render(request, 'index.html')

def userprofile_view(request):
    return render(request, 'profile.html')

def uploadblog_view(request):
    return render(request, 'upload.html')


class LogoutUser(LogoutView):
    template_name = 'logout.html'