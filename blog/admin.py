from django.contrib import admin
from blog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
  prepoluated_fields = {"slug":("title",)}
  list_display = ("slug","published_at")

class CommentAdmin(admin.ModelAdmin):
  list_display = ("creator","content")
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
