from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'

STATUS_CHOICE = (
    ('Draft','Draft'),
    ('Published','Published')
)
        
class Blogs(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True, blank=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=1000)
    blog_body = models.TextField(max_length=3000)
    status = models.CharField(max_length=100,choices=STATUS_CHOICE,default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Blogs'
        
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if empty
            self.slug = slugify(self.title)
            # Ensure slug is unique
            original_slug = self.slug
            counter = 1
            while Blogs.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
