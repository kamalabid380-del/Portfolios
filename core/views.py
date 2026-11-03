from django.shortcuts import render
from .models import Project, HeaderNav

def home(request):
    projects = Project.objects.all()
    navs = HeaderNav.objects.all()
    
    # Default profile - ye aapka naam dikhayega
    profile = {
        'name': 'Abid Kamal',
        'role': 'PYTHON & DJANGO WEB DEVELOPER',
        'bio': 'I build fast, clean, and modern web applications with Python & Django.',
    }

    return render(request, 'core/home.html', {
        'projects': projects, 
        'navs': navs,
        'profile': profile
    })

def blogs(request):
    return render(request, 'core/blogs.html')
