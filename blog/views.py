# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # return blog posts published up until now
    posts = Post.objects.filter(published_date__lte=timezone.now()
        # order by published date in descending order
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})

def post_detail(request, id):
    # id passed from url dispatcher
    # pass the post model and the id primary key to post variable.
    post = get_object_or_404(Post, pk=id)
    post.views +=1 # counter, adds 1 each time the post is viewed.
    post.save() # update the table with the incremented value.
    return render(request, "postdetail.html", {'post': post})