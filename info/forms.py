from django import forms
from .models import Info, Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "info",
                "class": "block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "Komentarz..",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ("body",)

class InfoForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "info",
                "class": "block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "Dodaj nową informację...",
            }
        ),
    )

    class Meta:
        model = Info
        fields = ("body",)
