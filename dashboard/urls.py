from django.urls import path
from . import views
from blogs import views as blogviews


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('categories/',views.categories, name="category_list"),
    path('categories/add',views.add_categories , name="add_category"),
    path('categories/edit/<int:pk>',views.edit_categories, name="edit_category"),
    path('categories/delete/<int:pk>',views.delete_categories, name="delete_category"),
]
