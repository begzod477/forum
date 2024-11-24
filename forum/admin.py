from django.contrib import admin

# Register your models here.

from .models import Comment, Topic, Reply

admin.site.register(Comment)
admin.site.register(Topic)
admin.site.register(Reply)


