from django.shortcuts import render,redirect,HttpResponse
from .models import Blogs,Category
from django.contrib import messages


# Create your views here.
def posts_by_category(requests,id):
    posts = Blogs.objects.filter(category=id,status="Published")
    try:
        category = Category.objects.get(pk=id)
    except:
        messages.error(requests," The Category was not found.")
        return redirect('home')
    context = {
        'posts':posts,
        'category':category,
    }

    return render(requests,'blogs/posts.html',context)

def getblog(request,slug):
    blog = Blogs.objects.get(slug=slug)
    context = {
        'blog':blog,
    }
    return render(request,'blogs/blog_single.html',context)