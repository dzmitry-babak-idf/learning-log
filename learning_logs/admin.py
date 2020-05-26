from django.contrib import admin
from .models import Topic, Entry,UserFile

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(UserFile)
# Register your models here.
