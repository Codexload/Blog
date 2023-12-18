from django.shortcuts import render
from Blog.models import Post, Category
from .forms import CommentForm
def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts':posts,
        'cats':cats,
    }
    return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    return render(request, 'posts.html', {'post':post, 'cats':cats})
def comment_view(request):
    commentform = CommentForm()
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            cd = commentform.cleaned_data
            print(cd)
    return render(request, 'home.html', {'commentform':commentform})