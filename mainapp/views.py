from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
import os
# Create your views here.
def index(request):
    return render(request, 'base_generic.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)  # Redirect to the post detail view
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    file_extension = os.path.splitext(post.file.name)[1].lower()
    is_image = file_extension in ['.jpg', '.jpeg', '.png', '.gif']
    return render(request, 'post_detail.html', {'post': post, 'is_image': is_image})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})