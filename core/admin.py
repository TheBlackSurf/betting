from django.contrib import admin
from .models import Post, Regulation, Vote, Profile, Kolejka
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin
from .models import Ankieta, Result

admin.site.register(Profile)
admin.site.register(Regulation)
admin.site.register(Result)
admin.site.register(Ankieta)


class KolejkaResource(resources.ModelResource):
    user = Field()

    class Meta:
        model = Kolejka
        fields = ('name', 'user', 'point')

    def dehydrate_user(self, obj):
        return obj.user.username


class KolejkasAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = KolejkaResource


admin.site.register(Kolejka, KolejkasAdmin)


# @admin.register(Kolejka, KolejkasAdmin)
# class KolejkaAdmin(admin.ModelAdmin):
#     '''Admin View for Kolejka'''

#     list_display = ('name', 'user', 'point')
#     list_filter = ('name', 'user')


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
