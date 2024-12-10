from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs", views.blogList, name="blogList"),
    path("readBlog/<int:id>/", views.readBlog, name="readBlog"),
    path("bdel/<int:id>/", views.deleteBlog, name="bDel"),
    path("cdel/<int:id>/<int:bid>/", views.deleteCom, name="cDel"),
    path("blike/<int:id>/", views.blike, name="blike"),
    path("bdlike/<int:id>/", views.bdlike, name="bdlike"),
]