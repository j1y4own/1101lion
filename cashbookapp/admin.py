from django.contrib import admin
from .models import Cashbook, Comment, Hashtag

admin.site.register(Cashbook)
admin.site.register(Comment)
admin.site.register(Hashtag)