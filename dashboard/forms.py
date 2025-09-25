from django import forms
from blogs.models import Category,Blogs

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = '__all__'
        
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blogs
        exclude = ['slug', 'author', 'is_featured', 'created_at', 'updated_at']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 3}),
            'blog_body': forms.Textarea(attrs={'rows': 6}),
        }