from django.urls import path
from . import views
from blogs import views as blogviews


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('blog/<slug:slug>/', views.blog_detail, name="blog_detail"),
    # category urls
    path('categories/',views.categories, name="category_list"),
    path('categories/add',views.add_categories , name="add_category"),
    path('categories/edit/<int:pk>',views.edit_categories, name="edit_category"),
    path('categories/delete/<int:pk>',views.delete_categories, name="delete_category"),
    # posts urls
    path('posts/',views.show_posts, name="show_posts"),
    path('posts/add',views.add_posts,name="add_post"),
    path('posts/delete/<int:pk>',views.delete_posts, name="delete_post"),
    path('posts/edit/<int:pk>',views.edit_posts,name="edit_post")
]
