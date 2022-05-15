
from django.db import models
from django.conf import settings

class Cookie(models.Model):
        user= models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
        coo=models.CharField(max_length=1000)