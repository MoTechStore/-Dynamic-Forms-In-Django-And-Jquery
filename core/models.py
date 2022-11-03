from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)




class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)


    def __str__(self):
        return self.title







class Records(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    opinion = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname



class Book(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    attachment = models.FileField(upload_to='')

    def __str__(self):
        return self.fname



class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    course = models.CharField(max_length=200)

    def __str__(self):
        return self.name



