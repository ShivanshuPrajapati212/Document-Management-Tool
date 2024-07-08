from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
import os
from mega import Mega
from django.conf import settings

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

            # Initialize Mega
            mega = Mega()
            m = mega.login(settings.MEGA_EMAIL, settings.MEGA_PASSWORD)

            # Upload file to Mega
            file = request.FILES['file']
            file_name = file.name
            mega_file = m.upload(file.temporary_file_path(), file_name)

            # Get the public link
            public_link = m.get_upload_link(mega_file)
            
            # Save the Mega link
            post.file = public_link
            post.save()

            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        # Initialize Mega
        mega = Mega()
        m = mega.login(settings.MEGA_EMAIL, settings.MEGA_PASSWORD)

        # Delete file from Mega
        file_path = post.file.split('!')[-1]  # Extract file path from Mega link
        m.destroy(file_path)

        # Delete post from database
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    file_extension = os.path.splitext(post.file.name)[1].lower()
    is_image = file_extension in ['.jpg', '.jpeg', '.png', '.gif']
    return render(request, 'post_detail.html', {'post': post, 'is_image': is_image})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})



def features(request):
    return render(request, 'features.html')