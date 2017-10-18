"""Djangoアドミン"""


from django.contrib import admin
# カレントディレクトリのmodels.pyから
from .models import Post, Comment


admin.site.register(Post)
admin.site.register(Comment)
