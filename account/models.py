from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    profile_pic = models.ImageField( upload_to="images/", null =True, blank = True, )
    line_1 = models.CharField( max_length=50, null=True, blank=True,)
    city = models.CharField(max_length= 200, null=True, blank=True,)
    state = models.CharField(max_length= 200, null=True, blank=True,)
    pincode = models.PositiveIntegerField(null=True, blank=True,)
    