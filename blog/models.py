from datetime import datetime
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
    slug = models.CharField(max_length=200, null=True, blank=True)
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




class Categories(models.Model):
    Categories = (
        ("Scripture", "Scripture"),
        ("Life", "Life"),
        ("Health", "Health"),
        ("Fashion", "Fashion"),
        ("Beauty", "Beauty"),
    )
    name = models.CharField(max_length=200, null=True, choices=Categories)
    image = models.ImageField(null=True, blank=True, upload_to="categories")

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class BlogArticles(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    articleCategory = models.ForeignKey(Categories, null=True, on_delete=models.CASCADE)
    ArticleImage = models.ImageField(null=True, blank=True, upload_to="blog")
    author = models.CharField(max_length=200, null=True, blank=True)
    AuthorImage = models.ImageField(null=True, blank=True, upload_to="blog")
    articleDescription = models.TextField(max_length=200, null=True, blank=True)
    article = models.TextField(max_length=10000, null=True, blank=True)
    ArticleImage1 = models.ImageField(null=True, blank=True, upload_to="blog")
    ArticleImage2 = models.ImageField(null=True, blank=True, upload_to="blog")
    ArticleImage3 = models.ImageField(null=True, blank=True, upload_to="blog")
    date_modified = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=False,editable=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog  Articles"

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.date_modified = datetime.now().date()
    #     super(BlogArticles, self).save(*args, **kwargs)

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


class About(models.Model):
    mainimage = models.ImageField(null=True, blank=True, upload_to="blog")
    intro_text = models.CharField(max_length=500, null=True, blank=True)
    goal = models.CharField(max_length=500, null=True, blank=True)
    paragraph_1 = models.TextField(max_length=10000, null=True, blank=True)
    paragraph_2 = models.TextField(max_length=10000, null=True, blank=True)
    paragraph_3 = models.TextField(max_length=10000, null=True, blank=True)
    paragraph_4 = models.TextField(max_length=10000, null=True, blank=True)
    Image1 = models.ImageField(null=True, blank=True, upload_to="blog")
    Image2 = models.ImageField(null=True, blank=True, upload_to="blog")


    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.goal


    @property
    def mainImage(self):
        try:
            url = self.mainimage.url
        except:
            url = ''
        return url

    @property
    def image1(self):
        try:
            url = self.Image1.url
        except:
            url = ''
        return url

    @property
    def image2(self):
        try:
            url = self.Image2.url
        except:
            url = ''
        return url

class BlogAim(models.Model):
    Indexer = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="about")
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Aim  of  Blog"

    def __str__(self):
        return self.title

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ContactUs(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    issue = models.TextField(max_length=10000, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=True)


    class Meta:
        verbose_name_plural = "Contact  Us"

    def __str__(self):
        return self.email