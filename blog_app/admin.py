from django.contrib import admin
from .models import *


# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title', 'category')
    filter_horizontal = ('tags', )


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, BlogPostAdmin)
admin.site.register(Comment)
