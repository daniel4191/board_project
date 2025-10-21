from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
    posts_all = Post.objects.all().order_by("-created")
    
    paginator = Paginator(posts_all, 10)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    latest_posts = posts_all[:3]
    context = {
        "page_obj":page_obj,
        "latest_posts": latest_posts
    }
    return render(request, "posts/post_list.html", context)

@login_required
def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect("posts:post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "posts/post_add.html", {"form": form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    comments = post.comment_set.all().order_by("created")
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("users:login")
        
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("posts:post_detail", pk=post.pk)
    
    else:
        comment_form = CommentForm()
    
    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form
    }
    
    return render(request, "posts/post_detail.html", context)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, writer=request.user)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            form.save()
            return redirect("posts:post_detail", pk=pk)
    
    else:
        form = PostForm(instance=post)
        
    return render(request, "posts/post_edit.html", {"form":form, "post":post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, writer=request.user)
    post.delete()
    return redirect("posts:post_list")

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("posts:post_detail", pk=comment.post.pk)
        
    else:
        form = CommentForm(instance=comment)
    return render(request,"posts/comment_edit.html", {"form":form, "comment":comment})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk , user= request.user)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("posts:post_detail", pk=post_pk)