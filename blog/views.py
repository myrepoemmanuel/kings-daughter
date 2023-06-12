import json
from json import dumps
from django.http import JsonResponse
from django.shortcuts import render
from .models import About, BlogAim, BlogArticles, ContactUs, Subscribers, WelcomeInformation, WhereToStart, Categories

# Create your views here.


def index(request):
    welcome_info = WelcomeInformation.objects.all()

    categories = Categories.objects.all()
    where_to_start = WhereToStart.objects.all()
    what_is_new = BlogArticles.objects.filter().order_by('-date_added')[:3]

    context = {
        'welcome_info':welcome_info,
        'where_to_start':where_to_start,
        'what_is_new': what_is_new,
        'categories':categories,
    }
    return render(request, 'blog/index.html', context)

def card(request):

    context = {

    }
    return render(request, 'blog/card.html', context)

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
    cat_name = Categories.objects.get(name=kwargs['category_name'])
    articles = BlogArticles.objects.filter(articleCategory=cat_name)
    latest_articles = BlogArticles.objects.filter().order_by('-date_added')[:4]

    context = {
        'articles':articles,
        'latest_articles':latest_articles
    }
    return render(request, 'blog/blog_category.html', context)


def about(request):
    about_text = About.objects.all()
    blog_aim = BlogAim.objects.all()

    context = {
        'about_text':about_text,
        'blog_aim':blog_aim,
    }
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

def podcast(request):

    context = {}
    return render(request, 'blog/podcast.html', context)


def subscribe(request):

    context = {}
    return render(request, 'blog/subscribe.html', context)



def processSubscriber(request):
    data = json.loads(request.body)


    Subscribers.objects.create(
    name=data['SubscriberData']['name'],
    email=data['SubscriberData']['email'],
    )


    return JsonResponse('subscriber added', safe=False)

def processContact(request):
    data = json.loads(request.body)


    ContactUs.objects.create(
    first_name=data['ContactData']['firstname'],
    last_name=data['ContactData']['lasttname'],
    email=data['ContactData']['email'],
    phone=data['ContactData']['phoneNumber'],
    country=data['ContactData']['country'],
    issue=data['ContactData']['subject'],
    )


    return JsonResponse('Contact added', safe=False)