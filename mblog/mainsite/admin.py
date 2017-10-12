from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'atype', 'pub_date')
    list_filter = ('atype', 'pub_date')


admin.site.register(Article, ArticleAdmin)
