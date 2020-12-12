from django.urls import path
from . import views
from .views import PVCreateView, GenerationForecast, \
    PVUpdateView, LoginView, Logout, PVDeleteView, PVDetailsView
from predictor.views import forecast_graph, get_n_days,forecast_result

urlpatterns = [

    path('about_us', views.AboutUsView.as_view(), name='about_us'),
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.PVCreateView.as_view(), name='create'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('forecast/', GenerationForecast.as_view(), name='forecast'),
    path('forecast_graph/', get_n_days, name='forecast_graph'),
    path('pv_plant_details/<int:pk>', views.pv_plant_details, name='pv_plant_details'),
    #path('pv_plant_details/<int:pk>', PVDetailsView.as_view(), name='pv_plant_details'),
    path('pv_plant_edit/<int:pk>', PVUpdateView.as_view(), name='edit'),
    path('pv_plant_delete/<int:pk>', PVDeleteView.as_view(), name='delete'),
    path('business_client/', views.BusinessView.as_view(), name='business_view'),

    path('login/', LoginView.as_view(), name='login user'),
    path('logout/',Logout.as_view(), name='logout user'),
]


