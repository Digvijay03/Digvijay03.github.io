from django.shortcuts import render

from .models import Post

# Create your views here.
def base(request):
    return render(request,'body/base.html')

def index(request):
    return render(request,'body/index.html')
def home(request):
    return render(request,'body/home.html')



def team(request):
    return render(request,'body/team.html')
def events(request):
    context = {
    'posts':Post.objects.all()
    }
    return render(request,'body/events.html',context)
def contact(request):
    return render(request,'body/contact.html')
def gallery(request):
    return render(request,'body/gallery.html')
