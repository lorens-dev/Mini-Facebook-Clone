from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required





# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
        
    #return HttpResponse('<h1> WELCOME HOME !!! </h1>')
    return render(request, 'fbclone/home.html', context)

def video(request):
    #return HttpResponse('<h1> THIS IS ABOUT PAGE </h1>') 
    return render(request, 'fbclone/video.html')

def marketplace(request):
    #return HttpResponse('<h1> THIS IS MARKET PLACE PAGE </h1>') 
    return render(request, 'fbclone/marketplace.html')

def groups(request):
    #return HttpResponse('<h1> THIS IS MARKET PLACE PAGE </h1>') 
    return render(request, 'fbclone/groups.html')

def gaming(request):
    #return HttpResponse('<h1> THIS IS MARKET PLACE PAGE </h1>') 
    return render(request, 'fbclone/gaming.html')
def home(request):
    # Fetch all posts (you might want to paginate or filter this)
    posts = Post.objects.all().order_by('-date_posted')  # Order by the date posted
    return render(request, 'fbclone/home.html', {'posts': posts})

def logout_view(request):
    logout(request)
    return render(request, 'user/logout.html')
@login_required
def video(request):
    return render(request, 'fbclone/video.html')

@login_required
def marketplace(request):
    return render(request, 'fbclone/marketplace.html')

@login_required
def groups(request):
    return render(request, 'fbclone/groups.html')

@login_required
def gaming(request):
    return render(request, 'fbclone/gaming.html')