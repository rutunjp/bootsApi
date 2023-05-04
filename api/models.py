from django.db import models
from django.contrib.auth.models import User 
class Boot(models.Model):
    modelName = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    price = models.IntegerField
    image =  models.ImageField(upload_to='products',blank=True, null=True )  
  



