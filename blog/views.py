from django.shortcuts import render, get_object_or_404 , HttpResponseRedirect 
from .models import Post
from .forms import CommentForm

# Create your views here.

def home(request):

    all_posts = Post.newmanager.all()

    return render(request, 'index.html', {'posts' : all_posts})

def post_single( request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    comments = post.comments.filter(status = True)

    comment_user = None

    if request.method == 'POST':
        comment_form = CommentForm (request.POST)

        if comment_form.is_valid():
            
            comment_user =  comment_form.save(commit = False)
            comment_user.post = post 
            comment_user.save()

            return HttpResponseRedirect('/' + post.slug) 

    else:
        comment_form = CommentForm ()
    return render(request, 
    'single.html', 
    {
        'post' : post ,
        'comment_form':comment_form ,
        'comments':comments ,
        },
    )