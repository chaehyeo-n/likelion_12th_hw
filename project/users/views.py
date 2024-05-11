from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.models import Post

# Create your views here.
def mypage(request):
    posts = Post.objects.all()
    return render(request, 'users/mypage.html', {'posts':posts})