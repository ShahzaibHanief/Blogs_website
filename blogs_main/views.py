from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True).order_by("updated_at")
    posts = Blog.objects.filter(is_featured = False , status = "Published")
    print(posts)
    # print(featured_posts)
    context ={
        "categories": categories,
        "featured_posts": featured_posts,
        "posts":posts
    }
    return render(request,'home.html',context)