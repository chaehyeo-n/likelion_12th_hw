from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('baskinrobbins', baskinrobbins, name="baskinrobbins"),
    path('reviews', reviews, name="reviews"),
    path('create', create, name="create"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('tag-list', tag_list, name="tag-list"),
    path('tag-posts/<int:tag_id>', tag_posts, name="tag-posts"),
    path('delete_comment/<int:id>', delete_comment, name="delete_comment"),
    path('likes/<int:post_id>', likes, name="likes")
]