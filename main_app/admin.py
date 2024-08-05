from django.contrib import admin

from blog_app.models import Category
from .models import *

# Register your models here.


admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Work)
admin.site.register(Service)
admin.site.register(Contact)
