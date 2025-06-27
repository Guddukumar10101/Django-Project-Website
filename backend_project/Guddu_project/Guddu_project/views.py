from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"homepage.html")

def about(request):
    return render(request,"about.html")

def Gallery(request):
    return render(request,"Gallery.html")

def Video(request):
    return render(request,"Video.html")


def Contact(request):
    return render(request,"Contact.html")

def Enquiry(request):
    return render(request,"Enquiry.html")
