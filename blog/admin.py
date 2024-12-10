from django.contrib import admin
from .models import Blog, Comment
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=("title", "author",)
    prepopulated_fields = {"slug": ("title", "author")}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
