"""Djangoアドミン"""


from django.contrib import admin
# カレントディレクトリのmodels.pyから
from .models import Post


admin.site.register(Post)
