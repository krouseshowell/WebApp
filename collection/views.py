from django.shortcuts import render, redirect
from collection.forms import BlogForm
from collection.models import Blogpost
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    #defining the variable
    return render(request, 'index.html',
    )

def blogpost_detail(request, slug):
    blogpost=Blogpost.objects.get(slug=slug)
    return render(request, 'blogposts/blog_details.html', {
        'blogpost': blogpost,
        })

@login_required
def edit_Blog(request, slug):
    blogpost = Blogpost.objects.get(slug=slug)
    if blogpost.user != request.user:
        raise Http404
    form_class = BlogForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=blogpost)
        if form.is_valid():
            form.save()
            return redirect('blogpost_detail', slug=blogpost.slug)
    else:
        form = form_class(instance=blogpost)

    return render(request, 'blogposts/edit_blogpost.html', {
        'blogpost': blogpost,
        'form': form,
    })

def create_blog(request):
    form_class = BlogForm
    if request.method == 'POST':
        form=form_class(request.POST)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.user = request.user
            blogpost.slug = slugify(blogpost.title)
            blogpost.save()
            return redirect('blogpost_detail', slug=blogpost.slug)
    else:
        form = form_class()
    return render(request, 'blogposts/create_blogpost.html', { 'form': form,})

def blog(request):
    blogposts = Blogpost.objects.all()
    return render(request, 'blog.html', {
        'blogposts': blogposts,
    })
