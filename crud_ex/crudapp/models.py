from django.db import models
class Students(models.Model):
    sid=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    mail=models.EmailField()
    contact=models.CharField(max_length=150)

# Create your models here.
