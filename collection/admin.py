from django.contrib import admin
from collection.models import Posts


class PostsAdmin(admin.ModelAdmin):
    model = Posts
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Posts, PostsAdmin)
