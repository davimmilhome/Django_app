from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_filter = ('status', 'criate','publicated','author')
    date_hierarchy = ('publicated')
    raw_id_fields = ('author',)
    list_display = ('title','author', 'publicated','status')
    prepopulated_fields = {'slug':('title',)}
# Register your models here.
