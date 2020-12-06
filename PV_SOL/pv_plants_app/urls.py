from django.urls import path
from . import views
from .views import login_user, logout_user, PVCreateView, GenerationForecast, \
    PVPlantUpdate, PVUpdateView  # register_user, forecast_generation,

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name="create"),
    #path('create/', views.PVCreateView.as_view(), name='create'),
    path('register/', views.RegisterView.as_view(), name='register'),
    #path('register/', register_user, name='register'),
    #path('forecast/', forecast_generation, name='forecast'), # just for now using register user for test only
    path('forecast/', GenerationForecast.as_view(), name='forecast'),
    path('pv_plant_details/<int:pk>', views.pv_plant_details, name='pv_plant_details'),
    path('pv_plant_edit/<int:pk>', views.pv_plant_edit, name='edit'),
    path('pv_plant_delete/<int:pk>', views.pv_plant_delete, name='delete'),
    #path('/pv_plant_delete/<int:pk>', views.pv_plant_delete, name='delete'),
    #path('PVUpdateView/<int:pk>', PVUpdateView.as_view(), name='edit'),
    path('login/', login_user, name='login user'),
    path('logout/',logout_user, name='logout user'),
]


#{% if pv_plant.can_edit %}
#<button class="btn btn-primary">Edit</button>
#{% endif %}