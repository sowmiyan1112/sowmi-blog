from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def home(request):
    info=Article.objects.filter().order_by('date')[0:7]
    return render(request,'articles/home.html',{'info':info})

def article_list(request):
    articles=Article.objects.all().order_by('number').reverse()
    return render(request,'articles/list.html', {'articles' : articles})


def article_details(request,slug):
    detail=Article.objects.get(slug=slug)
    return render(request,'articles/full_blog.html', {'detail':detail})

def about_me(request):
    return render(request, 'articles/about.html')