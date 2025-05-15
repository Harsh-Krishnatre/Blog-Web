from django import forms
from blogs.models import Category,Blogs
from django.utils.text import slugify


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = '__all__'
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'category', 'blog_image', 
                 'short_description', 'blog_body', 'status','is_featured']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
        
        if 'author' in self.fields:
            del self.fields['author']
        
        self.fields['blog_image'].required = False  
        self.fields['is_featured'].initial = False
        self.fields['is_featured'].widget = forms.HiddenInput()
    
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('slug') and cleaned_data.get('title'):
            cleaned_data['slug'] = slugify(cleaned_data['title'])
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:  # Set the author to current user
            instance.author = self.user
        if commit:
            instance.save()
        return instance