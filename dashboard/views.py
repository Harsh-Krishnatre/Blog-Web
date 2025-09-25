from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm
from django.contrib import messages
from django.contrib.auth.models import User

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
    messages.success(request,'Category has been deleted')
    return redirect('category_list')

@login_required(login_url='login')
def show_posts(request):
    if request.user.is_superuser:
        posts = Blogs.objects.all().order_by('-updated_at')
    else:
        posts = Blogs.objects.filter(author=request.user)
    context = {
        'posts':posts,
    }

    return render(request,'dashboard/posts/show_posts.html',context)

@login_required(login_url='login')
def add_to_featured(request,pk):
    if not request.user.is_superuser:
        return redirect('dashboard')
    post = get_object_or_404(Blogs,pk=pk)
    post.is_featured = True
    post.save()
    messages.success(request, f"'{post.title}' has been featured.")
    return redirect('show_posts')

@login_required(login_url='login')
def remove_from_featured(request, pk):
    # Security check: only superusers can perform this action
    if not request.user.is_superuser:
        return redirect('dashboard')

    post = get_object_or_404(Blogs, pk=pk)
    post.is_featured = False
    post.save()
    messages.success(request, f"'{post.title}' has been removed from featured.")
    return redirect('show_posts')

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
    messages.success(request,'Blogs successfully created')
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
    messages.success(request,'Blogs successfully deleted')
    return redirect('show_posts')

def users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'dashboard/users/users.html',context)


@login_required(login_url='login')
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST" and request.user.is_superuser:
        if request.user.id == user.id:
            messages.error(request, "You cannot delete your own account.")
        else:
            user.delete()
            messages.success(request, 'User has been deleted.')

    # Redirect to the user list for both GET and POST requests
    return redirect('user_list')