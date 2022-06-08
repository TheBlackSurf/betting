from django.contrib import admin
from .models import Post,Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''
    list_display = ('body', 'created_on', )

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    '''Admin View for Wynik'''
    list_display = ('name', 'author')
