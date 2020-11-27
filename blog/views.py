from django.shortcuts import render, get_object_or_404 , HttpResponseRedirect 
from .models import Post , Category
from .forms import CommentForm , FormSearch
from django.views.generic import ListView
from django.db.models import Q


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
class CategoryListView(ListView):

    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):

        content = {

            'cat': self.kwargs['category'],
            'posts':Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }

        return content


def category_list(request):

    category_list = Category.objects.exclude(name='default')

    context = {

        'category_list': category_list , 
    }

    return context




def search(request):
    
    form = FormSearch()
    
    results = []
    
    q = ''
    c = ''
    query = Q()
    form =FormSearch(request.GET)
    if "q" in request.GET and form.is_valid():
        
        q = form.cleaned_data['q']
        c = form.cleaned_data['c']
        if c is not None:
            query &=Q(category=c)
        if q is not None:
            query &=Q(title__contains=q)    
            
        results = Post.objects.filter(
                   query
           )
        
            
        
    return render (request , 'search.html' , {
        
        'form': form , 
        'q' : q , 
        'results' : results , 
    })            
