from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import BlogPost
from .forms import BlogPostForm
from django.http import HttpResponseRedirect
from datetime import datetime

# Create your views here.


def archive(request):
    posts = BlogPost.objects.all()[:10]
    return render(request, 'archive.html', {'posts': posts})


def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
            return HttpResponseRedirect('/blog/')
        else:
            form = BlogPostForm(request.POST)
            return render(request, 'create.html', {'form': form})
    else:
        form = BlogPostForm()
        return render(request, 'create.html', {'form': form})
