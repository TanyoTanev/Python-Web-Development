from django.urls import path
from . import views
from .views import login_user, logout_user, register_user

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name="create"),
    #path('register/', views.RegisterView.as_view(), name='register'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login user'),
    path('logout/',logout_user, name='logout user'),
]
