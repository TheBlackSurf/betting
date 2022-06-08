from django.contrib import admin
from .models import Post,Vote




@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    '''Admin View for Wynik'''
    list_display = ('name', 'author', 'post')
    list_filter = ('name',)

    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('body', 'created_on', )
    list_filter = ('body',)

    search_fields = ('body',)
