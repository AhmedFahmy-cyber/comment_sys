from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


def user_directory_path(instanse ,filename ):
    
    return "posts/{0}/{1}".format(instanse.id,filename)

def user_direc_day_path(instanse ,filename ):
    
    return "posts/%Y/%m/%d".format(instanse.id,filename)


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Post (models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT , default= 1)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to = 'posts/', default = 'posts/default.jpg')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    def get_absolute_url(self):
        return reverse('blog:post_single',args=[self.slug])

    def save(self, *args, **kwargs):
        #this line below give to the instance slug field a slug name
        self.slug = slugify(self.title)
        #this line below save every fields of the model instance
        super(Post, self).save(*args, **kwargs)  

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='comments')
    name =  models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField(max_length=500)
    publish = models.DateTimeField(auto_now_add=True)
    status =  models.BooleanField(default = True)


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        
        return f"comment by  {self.name}"

