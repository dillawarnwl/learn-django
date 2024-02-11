from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post, Comment
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'username', 'email', 'bio', 'password1', 'password2']
        labels = {
            'bio': 'Your Bio',
            'username':'Name',
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['img', 'title', 'body', 'categories']
        widgets = {
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }
