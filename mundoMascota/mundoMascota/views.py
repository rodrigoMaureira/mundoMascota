from cgitb import html
from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, "home.html")


def Tienda(request):

    return render(request, "Tienda.html")

def Blog(request):

    return render(request, "Blog.html")

def Contacto(request):

    return render(request, "Contacto.html")

def base(request):

    return render(request, "base.html")   

def Login(request):

    return render(request, "Login.html")

def Principal(request):

    return render(request, "Principal.html")