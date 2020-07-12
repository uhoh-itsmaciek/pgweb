from django.contrib import admin

from pgweb.util.admin import PgwebAdmin
from .models import NewsArticle, NewsTag


class NewsArticleAdmin(PgwebAdmin):
    list_display = ('title', 'org', 'date', 'modstate', )
    list_filter = ('modstate', )
    filter_horizontal = ('tags', )
    search_fields = ('content', 'title', )
    exclude = ('modstate', )


class NewsTagAdmin(PgwebAdmin):
    list_display = ('urlname', 'name', 'description')


admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(NewsTag, NewsTagAdmin)
