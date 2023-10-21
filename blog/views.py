from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def Likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

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

        liked = False
        if likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def Category(request, categories):
    category_posts = Post.objects.filter(category=categories)
    return render(request, "categories.html", {'categories': categories, "category_posts": category_posts})

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy("home")

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class MyPosts(ListView):
    model = Post
    template_name = 'my_posts.html'