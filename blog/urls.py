from django.urls import path
from .views import Home, PostDetail

urlpatterns = [
    #path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('post/<int:pk>', PostDetail.as_view(), name="post-details"),
]