from django.contrib import admin
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["author", "title"]
    list_display = ["author", "title"]


admin.site.register(Article, ArticleAdmin)