from django.urls import path
from . import views
from blogs import views as blogviews


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('categories/',views.categories, name="category_list"),
    path('categories/add',views.add_categories , name="add_category"),
]
