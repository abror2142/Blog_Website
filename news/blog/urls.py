from django.urls import path
from .views import (all_posts, all_posts_by_category_id, post_detail,
                    post_create, post_update, post_delete, category_create,
                    category_delete, category_detail, category_update)

urlpatterns = [
    path('', all_posts, name='index'),
    path('category/<int:category_id>/', all_posts_by_category_id, name='posts_by_category'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('add/', post_create, name='post_create'),
    path('update/<int:pk>/', post_update, name='post_update'),
    path('delete/<int:pk>/', post_delete, name='post_delete'),
    path('category-detail/<int:pk>/', category_detail, name='category_detail'),
    path('category-update/<int:pk>/', category_update, name='category_update'),
    path('category-create/', category_create, name='category_create'),
    path('category-delete/<int:pk>/', category_delete, name='category_delete')
]
