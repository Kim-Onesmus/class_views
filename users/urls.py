from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserLogin.as_view(),),
    path('homepage/', views.homepage_view,),
    path('profile/', views.userprofile_view,),
    path('new-blog/', views.uploadblog_view,),
    path('logout/', views.LogoutUser.as_view(),),
]