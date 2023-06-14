from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('blog/ourgiftcard/toyou/cyprine', views.card, name="card"),
    path('about/', views.about, name="about"),
    path('resources/', views.resources, name="resources"),
    path('contact/', views.contactus, name="contact"),
    # path('shop/', views.shop, name="shop"),
    path('blog/<str:article_title>', views.blogArticles, name="blog_articles"),
    path('comment/<str:comment>', views.blogComment, name="comments"),
    path('podcast/', views.podcast, name="podcast"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('process_subscriber/', views.processSubscriber, name="process_subscriber"),
    path('process_contact/', views.processContact, name="process_contact"),

    path('blog/category/<str:category_name>', views.blogCategorypage, name="blog_category_page"),

]