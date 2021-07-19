from django.db import models

# Create your models here.
class Horror(models.Model):
    Bookname=models.CharField(max_length=30)
    Author=models.CharField(max_length=30)
    Price=models.FloatField()
    Summary=models.CharField(max_length=700)
    Book=models.ImageField(upload_to='app_1/%y/%m/%d')


class Comic(models.Model):
    Bookname=models.CharField(max_length=30)
    Author=models.CharField(max_length=30)
    Price=models.FloatField()
    Summary=models.CharField(max_length=700)
    Book=models.ImageField(upload_to='app_1/%y/%m/%d')

class History(models.Model):
    Bookname=models.CharField(max_length=30)
    Author=models.CharField(max_length=30)
    Price=models.FloatField()
    Summary=models.CharField(max_length=700)
    Book=models.ImageField(upload_to='app_1/%y/%m/%d')

class Adventure(models.Model):
    Bookname=models.CharField(max_length=30)
    Author=models.CharField(max_length=30)
    Price=models.FloatField()
    Summary=models.CharField(max_length=700)
    Book=models.ImageField(upload_to='app_1/%y/%m/%d')