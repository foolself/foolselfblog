from django.contrib import admin

# Register
from blog.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created_date', 'published_date', )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


admin.site.register(Article, ArticleAdmin)
