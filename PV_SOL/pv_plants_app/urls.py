from django.urls import path
from . import views
from .views import login_user, logout_user, PVCreateView, GenerationForecast, \
    PVPlantUpdate, PVUpdateView, LoginView, Logout  # register_user, forecast_generation,
from predictor.views import  forecast_graph, get_n_days ,forecast_result

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name="create"),
    #path('create/', views.PVCreateView.as_view(), name='create'),
    path('register/', views.RegisterView.as_view(), name='register'),
    #path('register/', register_user, name='register'),
    #path('forecast/', views.pv_plant_forecast, name='forecast'),
    path('forecast/', GenerationForecast.as_view(), name='forecast'),
    path('forecast_graph/', get_n_days, name='forecast_graph'),
    path('pv_plant_details/<int:pk>', views.pv_plant_details, name='pv_plant_details'),
    path('pv_plant_edit/<int:pk>', views.pv_plant_edit, name='edit'),
    path('pv_plant_delete/<int:pk>', views.pv_plant_delete, name='delete'),
    path('business_client/', views.BusinessView.as_view(), name='business_view'),

    #path('/pv_plant_delete/<int:pk>', views.pv_plant_delete, name='delete'),
    #path('PVUpdateView/<int:pk>', PVUpdateView.as_view(), name='edit'),
    path('login/', LoginView.as_view(), name='login user'),
    path('logout/',Logout.as_view(), name='logout user'),
]


