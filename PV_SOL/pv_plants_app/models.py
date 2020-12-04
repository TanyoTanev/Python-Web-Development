from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models import ForeignKey

NULL_AND_BLANK = {'null': True, 'blank': True}

class PV_Plant(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    power = models.TextField()
    image = models.ImageField(max_length=250, upload_to='pv_plants')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULL_AND_BLANK)

class UserProfile(models.Model):
    date_of_birth = models.DateTimeField()
    profile_image = models.ImageField(
         upload_to="profiles/"
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)



    #