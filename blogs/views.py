from django.shortcuts import render,redirect
from .models import Blogs,Category
from django.contrib import messages


# Create your views here.
def posts_by_category(requests,id):
    categories = Category.objects.all()
    posts = Blogs.objects.filter(category=id,status="Published")
    try:
        category = Category.objects.get(pk=id)
    except:
        messages.error(requests," The Category was not found.")
        return redirect('home')
    context = {
        'categories':categories,
        'posts':posts,
        'category':category,
    }

    return render(requests,'blogs/posts.html',context)
