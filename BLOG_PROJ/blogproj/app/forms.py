from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Post, Comment
from django import forms


class SignUpUsers(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email ID'}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_author', 'post_title', 'post_content']

        widgets = {
            'post_author': forms.TextInput(attrs={'class': 'form-control'}),
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_content': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }
