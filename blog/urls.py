from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
    path('resources/', views.resources, name="resources"),
    path('contact/', views.contactus, name="contact"),
    path('shop/', views.shop, name="shop"),
    path('blog/<str:article_title>', views.blogArticles, name="blog_articles"),
    path('process_subscriber/', views.processSubscriber, name="process_subscriber"),

    path('blog/category/<str:category_name>', views.blogCategorypage, name="blog_category_page"),

]