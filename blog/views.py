from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm
# def home(request):
#     return render(request, 'index.html', {})

class Home(ListView):
    model = Post
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    # fields = ('title', 'body')

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm