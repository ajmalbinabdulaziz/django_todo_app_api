from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ToDO_Form
from .models import ToDo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        todo = ToDo.objects.filter(user=request.user, datecompleted=None)
        return render(request,'my_app/index.html', {'todos':todo})
    else:
        return render(request, 'my_app/index.html', {'error': 'Login Required'})   


def signup(request):
    if request.method == "GET":
        return render(request, 'my_app/signup.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']: 
            try:          
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                # return redirect('currenttodos')
                return redirect('index')
            except IntegrityError:
                return render(request, 'my_app/signup.html', {'form':UserCreationForm(), 'error':'The username has already been taken!'})


        else:
            return render(request, 'my_app/signup.html', {'form':UserCreationForm(), 'error':'Passwords did not match!'})


def login_page(request):
    if request.method == "POST":

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'my_app/login_page.html', {'form':AuthenticationForm(),'error': 'username and password did not match'})
        else:
            login(request, user)
            return redirect('index')
    else:
        return render(request, 'my_app/login_page.html', {'form': AuthenticationForm()}) 
    
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

@login_required
def createtodo(request):
    if request.method == "GET":
        return render(request, 'my_app/createtodo.html', {'form': ToDO_Form()})
    else:
        try:
            form = ToDO_Form(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('index')
        except ValueError:
            return render(request, 'my_app/createtodo.html', {'form': ToDO_Form(), 'error':'Please login and try again!'})


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(ToDo, pk=todo_pk, user=request.user)
    if request.method == "GET":        
        form = ToDO_Form(instance=todo)
        return render(request, 'my_app/viewtodo.html', {'todas': todo, 'form':form})
    else:
        try:
            form = ToDO_Form(request.POST, instance=todo)
            form.save()
            return redirect('index')
        except ValueError:               
            return render(request, 'my_app/viewtodo.html', {'todas': todo, 'form':form, 'error': 'Bad data passed in'})

@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(ToDo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('index')
         

@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(ToDo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('index')   


@login_required
def completed(request):
    todos = ToDo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request,'my_app/completed.html', {'todos':todos})


        





    







