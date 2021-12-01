from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,timedelta

# variables of a book
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    nbOfCopies = models.IntegerField()
    rating = models.IntegerField()
    description = models.TextField()
    id = models.IntegerField(primary_key=True)
    # datePublished = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("library:book-detail", kwargs={"book_id": self.id})


class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length = 100)
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length = 100)
    phoneNumber = models.CharField(max_length=8)
    # signUpDate = models.DateTimeField(auto_now_add = True)


class Librarian(models.Model):
    librarian = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length = 100)
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length = 100)
    phoneNumber = models.CharField(max_length=8)
    # signUpDate = models.DateTimeField(auto_now_add = True)

def get_return_date():
        return datetime.today() + timedelta(days=15)

class IssuedBook(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(default=get_return_date())

    def __str__(self):
        return self.Student.username + " borrowed " + self.Book.title
