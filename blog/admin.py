from django.contrib import admin
from blog.models import Tag, Post

class PostAdmin(admin.ModelAdmin):
  prepoluated_fields = {"slug":("title",)}
  list_display = ("slug","published_at")
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
# Register your models here.
