from django.shortcuts import render
from blogs.models import Category,Blogs


def home(requests): 
    featured_posts = Blogs.objects.filter(is_featured = True, status= 'Published')
    not_featured_posts = Blogs.objects.filter(is_featured = False,status = 'Published')
    context = {
        'featured' : featured_posts,
        'not_featured': not_featured_posts,
    }
    
    return render(requests,"home/home.html",context)