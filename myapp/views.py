from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from myapp.models import *

# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        mobile = request.POST['mobile']
        password = request.POST['password']
        email = request.POST['email']
        user = auth.models.User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('todo')
        else:
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def signout(request):
    auth.logout(request)
    return redirect('index')

def todo(request):
    task=todoitem.objects.all()
    return render(request, 'todo.html',{"task":task})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        date = request.POST.get('date')
        status='not started'
        todo=todoitem(title=title,updated_at=date,status=status).save()
        return redirect('todo')
    return render(request, 'todo.html')

def delete(request, str):
    todo = todoitem.objects.get(title=str)
    todo.delete()
    return redirect('todo')

def edit(request, str):
    todo = todoitem.objects.get(title=str)
    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        todo.title = title
        todo.updated_at = date
        todo.save()
        return redirect('todo')
    return render(request, 'edit_todo.html', {'todo': todo})

def search(request,str):
    
    if request.method == "POST":
        search=request.POST.get('search')
        if search:
            todoitem.objects.filter(search=str)
        return redirect('todo')
    return redirect('todo')