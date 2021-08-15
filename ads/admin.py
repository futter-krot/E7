from django.contrib import admin
from ads.models import Ad, Comment, Tag
# Register your models here.


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
