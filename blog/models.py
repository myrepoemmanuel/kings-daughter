import email
from pydoc import describe
from tabnanny import verbose
from django.db import models

# Create your models here.


class WelcomeInformation(models.Model):
    description = models.TextField(max_length=200, null=True, blank=True)
    titleImage = models.ImageField(null=True, blank=True, upload_to="welcome")
    ownerImage = models.ImageField(null=True, blank=True, upload_to="welcome")
    secondOwnerImage = models.ImageField(null=True, blank=True, upload_to="welcome")
    thirdOwnerImage = models.ImageField(null=True, blank=True, upload_to="welcome")

    class Meta:
        verbose_name_plural = "Welcome  Information"

    def __str__(self):
        return f'{self.id}'

    
    @property
    def TitleImage(self):
        try:
            url = self.titleImage.url
        except:
            url = ''
        return url
    
    @property
    def OwnerImage(self):
        try:
            url = self.ownerImage.url
        except:
            url = ''
        return url
    
    @property
    def SecondOwnerImage(self):
        try:
            url = self.secondOwnerImage.url
        except:
            url = ''
        return url
    
    @property
    def ThirdOwnerImage(self):
        try:
            url = self.thirdOwnerImage.url
        except:
            url = ''
        return url


class WhereToStart(models.Model):
    Indexer = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="welcome")
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Where  To  Start"

    def __str__(self):
        return self.title

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Subscribers(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email


class BlogArticles(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    articleCategory = models.CharField(max_length=200, null=True, blank=True)
    ArticleImage = models.ImageField(null=True, blank=True, upload_to="blog")
    author = models.CharField(max_length=200, null=True, blank=True)
    AuthorImage = models.ImageField(null=True, blank=True, upload_to="blog")
    articleDescription = models.TextField(max_length=200, null=True, blank=True)
    article = models.TextField(max_length=10000, null=True, blank=True)
    ArticleImage1 = models.ImageField(null=True, blank=True, upload_to="blog")
    ArticleImage2 = models.ImageField(null=True, blank=True, upload_to="blog")
    ArticleImage3 = models.ImageField(null=True, blank=True, upload_to="blog")
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog  Articles"

    def __str__(self):
        return self.title

    @property
    def articleImage(self):
        try:
            url = self.ArticleImage.url
        except:
            url = ''
        return url

    @property
    def authorImage(self):
        try:
            url = self.AuthorImage.url
        except:
            url = ''
        return url

    @property
    def image1(self):
        try:
            url = self.ArticleImage1.url
        except:
            url = ''
        return url
    
    @property
    def image2(self):
        try:
            url = self.ArticleImage2.url
        except:
            url = ''
        return url
    
    @property
    def image3(self):
        try:
            url = self.ArticleImage3.url
        except:
            url = ''
        return url