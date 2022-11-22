from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .forms import SignUpForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def home(request):
    
    return render(request, "main.html")
def signup(request):
    form =  SignUpForm

    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form':form}
 #   messages.success(request, form.errors)

    return render(request, "signup.html", context)

"""     
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            
            fname=request.POST.get('fname')
            sname=request.POST.get('sname')
            email=request.POST.get('email')
            password1=request.POST.get('password')
            user=authenticate(password=password1,email=email,fname=fname,sname=sname)
            form.save()
            print('user created')
   
        return (request,'signin.html')

     """

def signin(request):
    return render(request,"signin.html")
 
def signout(request):
    return render(request,"signout.html")
 