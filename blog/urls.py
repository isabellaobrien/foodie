from django.urls import path
from .views import Home, PostDetail, AddPost, UpdatePost, DeletePost, Likes, AddComment, MyPosts, AddCategory, Category

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('post/<int:pk>', PostDetail.as_view(), name="post-details"),
    path('add-post/', AddPost.as_view(), name="add-post"),
    path('add-category/', AddCategory.as_view(), name="add-category"),
    path('category/<str:categories>', Category, name="category"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="update-post"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name="delete-post"),
    path('likes/<int:pk>', Likes, name="like_post"),
    path('post/<int:pk>/comment', AddComment.as_view(), name="add-comment"),
    path('my-posts/', MyPosts.as_view(), name="my-posts"),
]