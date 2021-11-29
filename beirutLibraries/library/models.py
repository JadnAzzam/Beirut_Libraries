from django.db import models
from django.contrib.auth.models import User

# variables of a book
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    nbOfCopies = models.IntegerField()
    rating = models.IntegerField()
    description = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    datePublished = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return self.title


class Student(models.Model):
    client = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length = 100)
    phoneNumber = models.CharField(max_length=8)
    signUpDate = models.DateTimeField(auto_now_add = True)


class Librarian(models.Model):
    librarian = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length = 100)
    phoneNumber = models.CharField(max_length=8)
    signUpDate = models.DateTimeField(auto_now_add = True)

