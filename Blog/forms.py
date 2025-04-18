from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "tag"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your post title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Write your blog content here..."}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "tag": forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Add your comment..."})
        }
