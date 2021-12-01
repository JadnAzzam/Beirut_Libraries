from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegisterUserForm, RegisterLibrarianForm, UserForm, LibrarianForm, CreateBookForm, BookForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .models import Book, Student, Librarian
from django.db import models

@unauthenticated_user
def login_user_views(request):
  if request.method == "POST":
    form = AuthenticationForm(request = request, data = request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,f"You are now logged in as {username}")
            return redirect('')  ############# add views after login
        else:
            messages.error(request, 'Invalid Username or Password.')
    else:
        messages.error(request, "Invalid username or password.")
  form = AuthenticationForm() #returns form of login page 
  context = {'form':form}
  return render(request,'library/user_login.html',context)


def logout_user_views(request):
  logout(request)
  list(messages.get_messages(request))
  return redirect('home')

@unauthenticated_user
def register_user_views(request):
  if request.method == 'POST' :
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      username = form.cleaned_data.get('username')
      user_taken = Student.objects.filter(username = username).count()
      email = form.cleaned_data.get('email')
      email_taken = Student.objects.filter(email = email).count()
      if (user_taken != 0):
        messages.error(request,"Username taken, next time be creative!")
        return render(request, 'library/user_signup.html', {'form' : form})
      elif (email_taken != 0):
        messages.error(request,"This email already has an account.")
        return render(request, 'library/user_signup.html', {'form' : form})
      else:
        form.save()

        # group = Group.objects.get(name = 'user')
        # user.groups.add(group)
        # Student.objects.create(
        #   user = user,
        #   username = username,
        #   first_name = first_name,
        #   last_name = last_name,
        #   email = email,
        # )
        # messages.success(request, f"Account created successfully for {first_name}")
        return redirect('../../')

    else:
      
        for msg in form.error_messages:
          messages.error(request, f"{form.error_messages[msg]}")
        
        return render(request,'library/user_signup.html', {'form': form})     # returns signup page
  
  form = RegisterUserForm()
  return render(request, 'library/user_signup.html', {'form' : form})


  ### Librarian login view
@unauthenticated_user
def login_librarian_views(request):
  if request.method == "POST":
    form = AuthenticationForm(request = request, data = request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,f"Access to the library databases as {username}")
            return redirect('') ############# add views after login
        else:
            messages.error(request, 'Invalid Username or Password.')
    else:
        messages.error(request, "Invalid username or password.")
  form = AuthenticationForm() #returns form of login page 
  context = {'form':form}
  return render(request,'library/admin_login.html',context)


def logout_librarian_views(request):
  logout(request)
  list(messages.get_messages(request))
  return redirect('home')

@unauthenticated_user
def register_librarian_views(request):
  if request.method == 'POST' :
    form = RegisterLibrarianForm(request.POST)
    if form.is_valid():
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      username = form.cleaned_data.get('username')
      user_taken = Librarian.objects.filter(username = username).count()
      email = form.cleaned_data.get('email')
      email_taken = Librarian.objects.filter(email = email).count()
      if (user_taken != 0):
        messages.error(request,"Username taken, next time be creative!")
        return render(request, 'library/admin_signup.html', {'form' : form})  ### create admin_signup template
      elif (email_taken != 0):
        messages.error(request,"This email already has an account.")
        return render(request, 'library/admin_signup.html', {'form' : form})  ### create admin_signup template
      else:
        form.save()

        # group = Group.objects.get(name = 'user')
        # user.groups.add(group)
        # Student.objects.create(
        #   user = user,
        #   username = username,
        #   first_name = first_name,
        #   last_name = last_name,
        #   email = email,
        # )
        # messages.success(request, f"Account created successfully for {first_name}")
        return redirect('../../')

    else:
      
        for msg in form.error_messages:
          messages.error(request, f"{form.error_messages[msg]}")
        
        return render(request,'library/admin_signup.html', {'form': form})     # returns signup page
  
  form = RegisterLibrarianForm()
  return render(request, 'library/admin_signup.html', {'form' : form})
      
