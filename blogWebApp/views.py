from django.shortcuts import render
from blogs.models import Category,Blogs


def home(requests): 
    categories = Category.objects.all()
    featured_posts = Blogs.objects.filter(is_featured = True, status= 'Published')
    not_featured_posts = Blogs.objects.filter(is_featured = False,status = 'Published')
    context = {
        'categories':categories,
        'featured' : featured_posts,
        'not_featured': not_featured_posts,
    }
    
    return render(requests,"home/base.html",context)