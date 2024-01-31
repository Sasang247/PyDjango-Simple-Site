from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Courses(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField()
    description=HTMLField()

   
   

class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='blog')
    description=HTMLField()

class Contact(models.Model):

    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    message=models.TextField()

    def __str__(self):
        return "Message from " + self.fname 
        
class Carrer(models.Model):
    title=models.CharField(max_length=50)
    address=models.CharField(max_length=30)

class Apply(models.Model):
    fname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    message=models.TextField()
    cv = models.FileField(upload_to='apply')

    def __str__(self):
        return "Job Apply from " + self.fname


    


