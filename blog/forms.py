from django import forms
from .models import Post, Comment, Category, Difficulty

choices = Category.objects.all().values_list("name", "name")
choice_list = []

for item in choices:
    choice_list.append(item)

levels = Difficulty.objects.all().values_list("level", "level")
level_list = []

for item in levels:
    level_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'excerpt', 'category', 'difficulty', 'body', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value': '', 'id': 'bella', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'difficulty': forms.Select(choices=level_list, attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }