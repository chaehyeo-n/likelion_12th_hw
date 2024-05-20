from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post, Comment, Tag

# Create your views here.

def mainpage(request):
    return render(request, 'main/mainpage.html')

def baskinrobbins(request):
    posts = Post.objects.all()
    return render(request, 'main/baskinrobbins.html', {'posts':posts})

def reviews(request):
    return render(request, 'main/reviews.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post':post, 'comments':comments})

    elif request.method == 'POST':
        new_comment = Comment()

        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()

        new_comment.save()
        return redirect('main:detail', id)

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post': edit_post})

def create(request):
    if request.user.is_authenticated:
        new_post = Post()

        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.flavor = request.POST['flavor']
        new_post.body = request.POST['body']
        new_post.pub_date = timezone.now()
        new_post.image = request.FILES.get('image')

        new_post.save()

        words = new_post.body.split(' ')
        tag_list = []

        for w in words:
            if len(w)>0:
                if w[0] == '#':
                    tag_list.append(w[1:])

        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)

        return redirect('main:detail', new_post.id)
    
    else:
        return redirect('accounts:login')

def update(request, id):
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.writer:

        update_post.title = request.POST['title']
        update_post.flavor = request.POST['flavor']
        update_post.body = request.POST['body']
        update_post.pub_date = timezone.now()
    
        if request.FILES.get('image'):
            update_post.image = request.FILES.get['image']

        update_post.save()

        return redirect('main:detail', update_post.id)
    return redirect('accounts:login', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(pk=id)

    delete_post.delete()
    return redirect('main:baskinrobbins')
    
def delete_comment(request, id):
    delete_comment = Comment.objects.get(pk=id)
    post_id = delete_comment.post.id
    delete_comment.delete()
    return redirect('main:detail', id=post_id)

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', { 'tags' : tags })

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag-post.html', {
        'tag' : tag,
        'posts' : posts
    })