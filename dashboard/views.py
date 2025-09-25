from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm


# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    
    context = {
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request, 'dashboard/categories.html')

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
    return render(request,'dashboard/add_categories.html',context)

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
    
    return render(request,'dashboard/edit_categories.html',context)

def delete_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('category_list')

def show_posts(request):
    posts = Blogs.objects.filter(author=request.user)
    context = {
        'posts':posts,
    }

    return render(request,'dashboard/posts/show_posts.html',context)

def add_posts(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.is_featured = False
            blog.slug = blog.generate_unique_slug()
            blog.save()
            return redirect('show_posts')
    else:
        form = BlogForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/posts/add_posts.html',context)

def edit_posts(request,pk):
    post = get_object_or_404(Blogs,pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            title = form.cleaned_data['title']
            post.slug = post.generate_unique_slug()
            post.save()
            return redirect('show_posts')
    form = BlogForm(instance=post)
    context = {
        'form':form,
        'post':post
    }
    return render(request,'dashboard/posts/edit_posts.html',context)

def delete_posts(request,pk):
    post = get_object_or_404(Blogs,pk=pk)
    post.delete()
    return redirect('show_posts')