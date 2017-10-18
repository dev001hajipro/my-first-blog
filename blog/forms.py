from django import forms

from .models import Post, Comment

# Djangoはモデルフォーム機能でモデルからフォームを簡単に作成できる。
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', )