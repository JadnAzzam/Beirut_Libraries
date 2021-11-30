from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegisterUserForm, RegisterLibrarianForm, UserForm, LibrarianForm, CreateBookForm, BookForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .models import Book, Student, Librarian, post, Lost
from django.db import models
from social import forms

@unauthenticated_user
def login_user_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request = request, data = request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,f"You are now logged in as {username}")
            return redirect('/')
        else:
            messages.error(request, 'Invalid Username or Password.')
    else:
        messages.error(request, "Invalid username or password.")
  form = AuthenticationForm()
  #returns the login page
  context = {'form':form}
  return render(request,'main/login.html',context)


def logoutUser(request):
  logout(request)
  list(messages.get_messages(request))
  return redirect('login')
