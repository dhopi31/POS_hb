from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    context = {
        'judul' : 'Home'
    }
    
    return render(request, 'main.html' , context)

def contact(request):

    context = {
        'judul' : 'Contact'
    }
    
    return render(request, 'contact.html' , context)