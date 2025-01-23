from django import forms
from post.models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'message', 'category', 'image']
        # fields = "__all__"

