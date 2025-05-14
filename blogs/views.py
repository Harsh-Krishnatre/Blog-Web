from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
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
        'active_category':category,
        'posts':posts,
    }

    return render(requests,'blogs/blog_list.html',context)

def getblog(request,slug):
    blog = get_object_or_404(Blogs, slug=slug, status='Published')
    context = {
        'blog':blog,
    }
    return render(request,'blogs/blog_single.html',context)

def search(request):
    keyword = request.GET.get('keyword','')
    results = Blogs.objects.filter(title__icontains=keyword) if keyword else []
    context = {
        'posts':results,
    }
    return render(request,'blogs/blog_list.html',context)