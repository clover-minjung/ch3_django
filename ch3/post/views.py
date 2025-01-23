from django.shortcuts import get_object_or_404, render, redirect

from post.models import Post, Category
from post.forms import PostForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST


def category_list(request):
    categories = Category.objects.all()
    no_category_posts = Post.objects.filter(category__isnull=True)  # 카테고리 없는 글
    context = {
        'categories': categories,
        'no_category_posts': no_category_posts,
    }
    return render(request, 'post/category_list.html', context)

def category_detail(request, category_id):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        posts = category.category_posts.filter(category=category)  # related_name='category_posts' 사용
    else:  # 카테고리 없는 글 보기
        category = None
        posts = Post.objects.filter(category__isnull=True)    
    context = {
        'category': category, 'posts': posts
    }
    return render(request, 'post/category_detail.html', context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request=request, template_name='post/post_list.html', context=context)

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    referer = request.META.get('HTTP_REFERER')  # 이전 경로 가져오기
    context = {
        'post': post,
        'referer': referer
    }
    return render(request=request, template_name='post/post_detail.html', context=context)


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post:post_detail", post.id)
    else:
        form = PostForm()
    return render(request=request, template_name='post/post_form.html', context={'form': form})

@login_required
@require_http_methods(["GET", "POST"])
def post_update(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post:post_detail", post.pk)
    else:
        form = PostForm(instance=post)
    # form: 글 작성/수정을 위한 입력 폼 데이터, post: 작성과 수정 상태를 구분하기 위해 사용
    context = {
        "form": form,
        "post": post,
    }
    return render(request=request, template_name="post/post_form.html", context=context)

# @require_POST
# @login_required 또는 is_authenticated
def post_delete(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            post.delete()
            return redirect('post:post_list')
    return render(request, 'post/post_delete.html', {'post': post})
