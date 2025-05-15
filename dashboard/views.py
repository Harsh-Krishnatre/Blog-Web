from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm
from django.utils.text import slugify


# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    
    context = {
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    
    return render(request,'dashboard/base.html',context)

def categories(request):
    return render(request, 'dashboard/categories/categories.html')

def add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    context = {
        'form':form,
    }
    return render(request,'dashboard/categories/add_categories.html',context)

def edit_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form':form,
        'categories':category,
    }
    
    return render(request,'dashboard/categories/edit_categories.html',context)

def delete_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('category_list')

def show_posts(request):
    posts = Blogs.objects.filter(author=request.user.id)
    context = {
        'posts':posts,
        'name':request.user.username,
    }
    return render(request,'dashboard/posts/show_posts.html',context)

def add_posts(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,user=request.user)
        if form.is_valid():
            temp = form.save(commit=False)
            if not temp.slug:
                temp.slug = slugify(temp.title)
            temp.save()
            return redirect('blog_detail', slug=temp.slug)
    else:
        form = BlogForm(user=request.user)
    context = {
        'form':form,
    }
    return render(request,'dashboard/posts/add_posts.html',context)

def delete_posts(request,pk):
    category = get_object_or_404(Blogs,pk=pk)
    category.delete()
    return redirect('show_posts')

def blog_detail(request, slug):
    try:
        blog = Blogs.objects.get(slug=slug)
        context = {
            'blog': blog,
        }
        return render(request, 'blogs/blog_single.html', context)
    except Blogs.DoesNotExist:
        # You could log the error here
        raise Http404("Blog post does not exist")

def edit_posts(request,pk):
    posts = get_object_or_404(Blogs,pk=pk)
    if request.method=="POST":
        form = BlogForm(request.POST,request.FILES,user=request.user,instance=posts)
        if form.is_valid():
            form.save()
            return redirect('show_posts')
    else:
        form = BlogForm(instance=posts)
    context = {
        'form':form,
        'post':posts,
    }
    return render(request,'dashboard/posts/edit_posts.html',context)