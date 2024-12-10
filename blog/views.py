from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import Blog, Comment, Blike, Bdislike, Clike, Cdislike
from .forms import BlogForm, CommentForm
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}

    return render(request, 'home.html', context)

def blogList(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(author=request.user)
        if request.method == "POST":
            form = BlogForm(request.POST)
            if form.is_valid():
                nb = form.save(commit=False)
                nb.setPostDate()
                nb.setAuthor(request.user)
                nb.setContPrev()
                nb.save()
        else:
            form = BlogForm()
        context = {'blogs': blogs, 'form': form}
        return render(request, 'blogList.html', context)
        
    else:
        return redirect('user:login')
    
def readBlog(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                nc = form.save(commit=False)
                nc.setAuthor(request.user)
                nc.setBlog(Blog.objects.get(pk=id))
                nc.setPostDate()
                nc.save()
        else:
            form = CommentForm()
        try:
            b = Blog.objects.get(pk=id)
            coms = b.comment_set.all()

        except ObjectDoesNotExist:
            return redirect('home')
        
        context = {'blog': b, 'coms': coms, 'form': form}
        return render(request, 'readBlog.html', context)
    else:
        try:
            b = Blog.objects.get(pk=id)
            coms = b.comment_set.all()
            context = {'blog': b, 'coms': coms}
            
            return render(request, 'readBlog.html', context)
        
        except ObjectDoesNotExist:
            return redirect('home')
    
    
def deleteBlog(request, id):
    if request.user.is_authenticated:
        b = Blog.objects.get(pk=id)
        if b.author == request.user:
            b.delete()
            return redirect('blogList')
        else:
            return redirect('home')
    else:
        return redirect('user:login')
    
def deleteCom(request, id, bid):
    if request.user.is_authenticated:
        c = Comment.objects.get(pk=id)
        if c.cAuthor == request.user:
            c.delete()
            return redirect(reverse('blogList', kwargs={'id': bid}))
        else:
            return redirect('home')
    else:
        return redirect('user:login')

def blike(request, id):
    if request.user.is_authenticated:
        b = Blog.objects.get(pk=id)
        try:
            bl = Blike.objects.get(user=request.user, blog=b)
            bl.delete()
        except ObjectDoesNotExist:
           nbl = Blike(user=request.user, blog=b)
           nbl.save()

        try:
            bd = Bdislike.objects.get(user=request.user, blog=b)
            bd.delete()
        except ObjectDoesNotExist:
            pass

        return redirect('home')
    else:
        return redirect('home')
    
def bdlike(request, id):
    if request.user.is_authenticated:
        b = Blog.objects.get(pk=id)
        try:
            bd = Bdislike.objects.get(user=request.user, blog=b)
            bd.delete()
        except ObjectDoesNotExist:
            nbd = Bdislike(user=request.user, blog=b)
            nbd.save()

        try:
            bl = Blike.objects.get(user=request.user, blog=b)
            bl.delete()
        except ObjectDoesNotExist:
            pass 

        return redirect('home')
    else:
        return redirect('home')