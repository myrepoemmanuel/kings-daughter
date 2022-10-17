from django.contrib import admin
from .models import WelcomeInformation, WhereToStart, Subscribers, BlogArticles

# Register your models here.

admin.site.register(Subscribers)
admin.site.register(WhereToStart)
admin.site.register(WelcomeInformation)
admin.site.register(BlogArticles)