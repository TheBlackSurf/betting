from django.contrib import admin
from .models import Post, Vote, Profile, Kolejka

admin.site.register(Profile)

@admin.register(Kolejka)
class KolejkaAdmin(admin.ModelAdmin):
    '''Admin View for Kolejka'''

    list_display = ('name', 'user', 'point')
    list_filter = ('name', 'user')



@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    """Admin View for Wynik"""

    list_display = ("name", "author", "post")
    list_filter = ("name",)

    search_fields = ("name", "created_on")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post"""

    list_display = (
        "body",
        "created_on",
    )
    list_filter = ("body",)

    search_fields = ("body",)
