from django.contrib import admin
from .models import Tag, Author, Article, Track

# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Track)