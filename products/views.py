from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import product

def index(request):
    return render(request,'index.html')

def signup(request):
    #checking if any data is entered ir not
    if request.method=='POST':
        #checking the two entered passwords are correct or not
        if request.POST['password1']==request.POST['password2']:
            #checking the entered username is already present or not
            #in this we are using .get function and we will get the Username
            #else we will get an error called 'User.DoesNotExist'
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'You entered username is already exist'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('index')
        else:
            return render(request,'signup.html',{'error':'You entered password is Incorrect'})

    else:
        return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return render(request,'login.html',{'error':'username or password is Incorrect'})

    else:
        return render(request,'login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')

def create(request):
    if request.method=='POST':
        user=product()
        #users=product.objects.get_or_create(title=request.POST['title'],body=request.POST['body'],url=request.POST['url'],icon=request.FILES['icon'],image=request.FILES['image'],hunter=request.user)[0]
        user.title=request.POST['title']
        user.body=request.POST['body']
        user.url=request.POST['url']
        user.icon=request.FILES['icon']
        user.image=request.FILES['image']
        user.hunter=request.user
        user.save()
        return redirect('index')
    else:
        return render(request,'create.html')
