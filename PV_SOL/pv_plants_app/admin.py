from django.contrib import admin
from .models import PV_Plant, UserProfile

# Register your models here.
admin.site.register(PV_Plant)
admin.site.register(UserProfile)