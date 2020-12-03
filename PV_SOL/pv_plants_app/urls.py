from django.urls import path
from . import views
from .views import login_user, logout_user, forecast_generation, PVCreateView, GenerationForecast  # register_user,

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name='index'),
    #path('create/', views.create, name="create"),
    path('create', PVCreateView.as_view(), name='create'),
    path('register/', views.RegisterView.as_view(), name='register'),
    #path('register/', register_user, name='register'),
    #path('forecast/', forecast_generation, name='forecast'), # just for now using register user for test only
    path('forecast/', GenerationForecast.as_view(), name='forecast'),
    path('login/', login_user, name='login user'),
    path('logout/',logout_user, name='logout user'),
]
