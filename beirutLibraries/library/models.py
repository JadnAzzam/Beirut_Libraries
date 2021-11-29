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



# book forms code 

# from django import forms
# from .models import Book

# class BookForm(forms.ModelForm):
#     title        = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Book title"}))
#     author       = forms.CharField()
#     description  = forms.CharField(required=False, widget = forms.Textarea(
#         attrs={
#             "placeholder": "Book description",
#             "class": "new-class-name two",
#             "id": "my-id-for-textarea",
#             "rows": 10,
#             "cols": 30,
#             }
#         )
#     )
#     class Meta:
#         model = Book
#         fields = [
#             'title',
#             'author',
#             'description',
#         ]



# Book models code 

# from django.db import models
# from django.urls import reverse

# # Create your models here.

# class Book(models.Model):
#     title       = models.CharField(max_length = 100) #max_length is required for CharField
#     author      = models.CharField(max_length = 100)
#     description = models.TextField() 

#     def get_absolute_url(self):
#         return reverse("book:book-detail", kwargs={"book_id": self.id})






