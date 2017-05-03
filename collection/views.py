from django.shortcuts import render
from collection.models import Blogpost

# Create your views here.
def index(request):
    #defining the variable
    blogposts = Blogpost.objects.all()
    return render(request, 'index.html', {
        'blogposts': blogposts,
    })
