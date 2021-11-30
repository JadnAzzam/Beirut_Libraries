from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegisterUserForm, RegisterLibrarianForm, UserForm, LibrarianForm, CreateBookForm, BookForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
##from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .models import Book, Student, Librarian
