from django.urls import path
from . import views
from blogs import views as blogviews


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    # Category Paths
    path('categories/',views.categories, name="category_list"),
    path('categories/add/',views.add_categories , name="add_category"),
    path('categories/edit/<int:pk>/',views.edit_categories, name="edit_category"),
    path('categories/delete/<int:pk>/',views.delete_categories, name="delete_category"),
    # Post Paths
    path('posts/',views.show_posts, name="show_posts"),
    path('posts/add/',views.add_posts,name="add_post"),
    path('posts/edit/<int:pk>',views.edit_posts,name="edit_posts"),
    path('posts/delete/<int:pk>',views.delete_posts,name="delete_posts"),
    path('posts/add_to_featured/<int:pk>/', views.add_to_featured, name='add_to_featured'),
    path('posts/remove_from_featured/<int:pk>/', views.remove_from_featured, name='remove_from_featured'),

    #path for users
    path('users/',views.users, name="user_list"),
    path('users/delete/<int:pk>',views.delete_user, name="delete_user"),
]
