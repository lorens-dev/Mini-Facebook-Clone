from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
        
    #return HttpResponse('<h1> WELCOME HOME !!! </h1>')
    return render(request, 'fbclone/home.html', context)

def about(request):
    #return HttpResponse('<h1> THIS IS ABOUT PAGE </h1>') 
    return render(request, 'fbclone/about.html')

def marketplace(request):
    #return HttpResponse('<h1> THIS IS MARKET PLACE PAGE </h1>') 
    return render(request, 'fbclone/marketplace.html')