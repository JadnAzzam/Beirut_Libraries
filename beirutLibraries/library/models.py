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

class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
