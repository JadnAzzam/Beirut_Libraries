from django import forms
from django.forms.models import ModelForm
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Create new User:
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2") 

    def save(self, commit=True):
        student = super(RegisterUserForm, self).save(commit=False)
        student.email = self.cleaned_data["email"]
        if commit:
            student.save()
        return student


#Change User infos:
class UserForm(ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'
        exclude = ['user', 'id']


#Create new Librarian:
class RegisterLibrarianForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2") 

    def save(self, commit=True):
        librarian = super(RegisterLibrarianForm, self).save(commit=False)
        librarian.email = self.cleaned_data["email"]
        if commit:
            librarian.save()
        return librarian


#Change Librarian infos:
class LibrarianForm(ModelForm):
    class Meta:
        model = models.Librarian
        fields = '__all__'
        exclude = ['user', 'id']


#Create new Book:
class CreateBookForm(forms.ModelForm):
    title        = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Book title"}))
    author       = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Author"}))
    nbOfCopies   = forms.IntegerField()
    rating       = forms.IntegerField()
    description  = forms.CharField(required=False, widget = forms.Textarea(attrs={"placeholder": "Book description",}))
    class Meta:
        model = models.Book
        fields = [
            'title',
            'author',
            'description',
            'nbOfCopies',
            'rating',
        ]


#edit Book:
class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        exclude = ['id']


class Book_IssueForm(forms.ModelForm):
    class Meta:
        model=models.IssuedBook
        exclude = ['issue_date', 'return_date']

