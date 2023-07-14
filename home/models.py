from django.db import models
 
# Create your models here.
class data1(models.Model):
    Datetime= models.DateField()
    High=models.FloatField()

class Meta:
    ordering=('DateTime')

