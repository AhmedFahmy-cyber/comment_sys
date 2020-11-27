from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.search, name='search'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CategoryListView.as_view(), name='category'),
]