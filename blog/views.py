"""ビュー
"""
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import PostForm
from .models import Post

# Create your views here.

def post_list(request):
    """記事一覧"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """記事詳細画面"""
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    """記事新規作成"""
    if request.method == "POST":
        # これはフォームオブジェクト
        form = PostForm(request.POST) # formのデータを取得
        if form.is_valid():
            # デフォルトはcommit=Trueで、フォームをデータベースに保存する
            # 保存する前に何か処理をしたい場合、form.save(commit=False)で
            # モデルオブジェクトを取得できる。
            post = form.save(commit=False)
            post.author = request.user
            # 公開日に値を入れずに、ドラフト（下書き)で保存する。
            #post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    """記事更新"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # 保存処理
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # 公開日に値を入れずに、ドラフト（下書き)で保存する。
            #post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        # /post/10/edit/でGETリクエストが来た場合、編集フォームを用意する。
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    """下書き一覧"""
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    """公開"""
    post = get_object_or_404(Post, pk=pk)
    post.publish()  # 公開日を設定する。
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    """削除"""
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')