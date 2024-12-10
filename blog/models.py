import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    #Title of the Blog
    title = models.CharField(max_length=150)
    
    #Date the Blog was originally posted auto set by the view
    date_posted = models.DateTimeField()

    #Date the Blog was last edited. 
    #Will initially be blank until the author edits the Blog 
    #then will be set the same as date posted
    date_last_edited = models.DateTimeField(blank=True, null=True)

    #The text content of the Blog post
    content = models.TextField(max_length=3000)

    #snippet of blog content to be displayed on home page
    cont_prev = models.CharField(max_length=80, default="")

    #The user that created the Blog
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #for URL readability
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.title
    
    def was_posted_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)
    
    def setPostDate(self):
        self.date_posted = timezone.now()

    def setEditDate(self, dt):
        self.date_last_edited = dt

    def setAuthor(self, user):
        self.author = user    

    def setContPrev(self):
        self.cont_prev = self.content[0:77] + "..."
    


class Comment(models.Model):
    #the user that created the comment
    cAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    #the blog the comment is attached to
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    #the text content of the comment
    content = models.TextField(max_length=250)
    
    #date the comment was posted
    date_posted = models.DateTimeField()
    

    def __str__(self):
        return self.content
    
    def setBlog(self, blog):
        self.blog = blog  
    
    def setAuthor(self, user):
        self.cAuthor = user  

    def setPostDate(self):
        self.date_posted = timezone.now()
    
    def was_posted_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)
    
class Blike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Clike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    com = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Bdislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Cdislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    com = models.ForeignKey(Comment, on_delete=models.CASCADE)