from django.contrib import admin
from article.models import Article, Comment, ReplyComment


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ReplyComment)


