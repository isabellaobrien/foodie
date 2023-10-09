from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# def home(request):
#     return render(request, 'index.html', {})

def Likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))


class Home(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-date']

class PostDetail(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data()
        likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes.total_likes()
        context["total_likes"] = total_likes
        return context


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

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')