from django import forms

from .models import Post

# Djangoはモデルフォーム機能でモデルからフォームを簡単に作成できる。
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)