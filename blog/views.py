# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # return blog posts published up until now
    posts = Post.objects.filter(published_date_lte=timezone.now()
        # order by published date in descending order
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})