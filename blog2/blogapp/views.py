from django.shortcuts import render
from .models import Courses , Blog ,Contact ,Carrer ,Apply
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'blogapp/home.html')

def services(request):
    courses=Courses.objects.all()
    return render(request,'blogapp/services.html',{'courses':courses})

def joinus(request):
    return render(request,'blogapp/joinus.html')

def blog(request):
    blogs=Blog.objects.all()
    return render(request,'blogapp/blog.html',{'blogs':blogs})

def about(request):
    return render(request,'blogapp/about.html')

def buildwithus(request):
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data = Contact.objects.create(
            fname=fname,
            email=email,
            phone=phone,
            message=message
        )

        
        return render(request, 'blogapp/buildwithus.html', {'data': data})

    return render(request, 'blogapp/buildwithus.html')

def carrers(request):
    carrer=Carrer.objects.all()
    return render(request,'blogapp/carrers.html',{'carrer':carrer})

def internship(request):
    return render(request,'blogapp/internship.html')


def apply(request):
    if request.method == "POST":
        fname = request.POST['fname']
        address=request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data =Apply.objects.create(
            fname=fname,
            address=address,
            email=email,
            phone=phone,
            message=message
        )
      


    
        return render(request,'blogapp/apply.html',{'data':data})
    return render(request,'blogapp/apply.html')