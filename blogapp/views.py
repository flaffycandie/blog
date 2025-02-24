from django.shortcuts import render

from blogapp.models import BlogPost


# Create your views here.
def index(request):
    posts= BlogPost.objects.all()
    return render(request,'index.html',{'posts':posts})
