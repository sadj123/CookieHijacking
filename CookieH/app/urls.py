from nturl2path import url2pathname
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.Home, name="home"),
    path('login/', views.Login, name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
