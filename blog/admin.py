from django.contrib import admin
from .models import Comments, WelcomeInformation, WhereToStart, Subscribers, BlogArticles, Categories, About, BlogAim, ContactUs

# Register your models here.
admin.site.register(Categories)
admin.site.register(Subscribers)
admin.site.register(WhereToStart)
admin.site.register(WelcomeInformation)
admin.site.register(BlogArticles)

admin.site.register(About)
admin.site.register(BlogAim)
admin.site.register(Comments)


class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)

admin.site.register(ContactUs,ContactUsAdmin)
