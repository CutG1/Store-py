from django.contrib import admin

# Register your models here.

from .models import *




class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'views', 'created_at', 'update_at', 'publish')
    list_display_links = ('title',)
    list_editable = ('publish',)
    list_filter = ('title', 'category', 'update_at')



admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)