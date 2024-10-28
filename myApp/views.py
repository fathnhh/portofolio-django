from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def base(request):
    context = {
        'title': 'About Me',
    }
    return render(request, 'myApp/base.html', context)

def profil(request):
    context = {
        'title':'Profil',
    }
    return render(request, 'myApp/profil.html', context)

def education(request):
    context = {
        'title':'Education',
    }
    return render(request, 'myApp/education.html', context)

def experience(request):
    context = {
        'title':'Experience',
    }
    return render(request, 'myApp/experience.html', context)

def contact(request):
    context = {
        'title':'Contact',
    }
    return render(request, 'myApp/contact.html', context)