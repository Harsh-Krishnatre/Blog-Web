from django.shortcuts import render,redirect
from .models import Blogs,Category


# Create your views here.
def posts_by_category(requests,id):
    posts = Blogs.objects.filter(category=id,status="Published")
    try:
        category = Category.objects.get(pk=id)
    except:
        return redirect('home')
    context = {
        'posts':posts,
        'category':category,
    }

    return render(requests,'blogs/posts.html',context)
