from django.db import models
from django.contrib.auth.models import User

# variables of a book
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    nbOfCopies = models.IntegerField()
    rating = models.IntegerField(min_value = 1, max_value = 5)
    description = models.CharField(max_length=200)
    id = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    id = models.IntegerField()
    email = models.CharField(max_length = 100)
    phoneNumber = models.CharField(max_length=8)
    signUpDate = models.DateTimeField(auto_now_add = True)

