import json
from json import dumps
from django.http import JsonResponse
from django.shortcuts import render
from .models import BlogArticles, Subscribers, WelcomeInformation, WhereToStart

# Create your views here.


def index(request):
    welcome_info = WelcomeInformation.objects.all()

    welcome_intro = WhereToStart.objects.all()
    
    context = {
        'welcome_info':welcome_info,
        'welcome_intro':welcome_intro,
    }
    return render(request, 'blog/index.html', context)

def blog(request):
    articles = BlogArticles.objects.filter()
    latest_articles = BlogArticles.objects.filter().order_by('-date_added')[:4]
    
    print(latest_articles)
    context = {
        'articles':articles,
        'latest_articles':latest_articles,
    }
    return render(request, 'blog/blog.html', context)


def blogArticles(request, *args, **kwargs):
    articles = BlogArticles.objects.filter(title=kwargs['article_title'])
    latest_articles = BlogArticles.objects.filter().order_by('-date_added')[:4]

    

    context = {
        'articles':articles,
        'latest_articles':latest_articles,
    }
    return render(request, 'blog/article.html', context)


def blogCategorypage(request, *args, **kwargs):
    
    articles = BlogArticles.objects.filter(articleCategory=kwargs['category_name'])
    latest_articles = BlogArticles.objects.filter().order_by('-date_added')[:4]

    context = {
        'articles':articles,
        'latest_articles':latest_articles
    }
    return render(request, 'blog/blog_category.html', context)


def about(request):

    context = {}
    return render(request, 'blog/aboutus.html', context)



def resources(request):

    context = {}
    return render(request, 'blog/resources.html', context)


def contactus(request):

    context = {}
    return render(request, 'blog/contactus.html', context)


def shop(request):

    context = {}
    return render(request, 'blog/shop.html', context)


def processSubscriber(request):
    data = json.loads(request.body)
    
    
    Subscribers.objects.create(
    name=data['SubscriberData']['name'],
    email=data['SubscriberData']['email'],
    )


    return JsonResponse('payment complete', safe=False)