from dataclasses import field
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import *



class AnkietaForm(forms.ModelForm):
    class Meta:
        model = Ankieta
        fields = ('__all__')


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('choice',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("name", "surnname", "pic")


class VoteColorForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ("color_vote",)


class RegulationForm(forms.ModelForm):
    point = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "info",
                "class": "block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "Dodaj nowy punkt...",
            }
        ),
    )

    class Meta:
        model = Regulation
        fields = ("point",)


class RFPAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={"class": "form-control input-sm",
                   "placeholder": "Nazwa Użytkownika"}
        )
    )
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "type": "password",
                "name": "password",
                "class": "form-control input-sm",
                "placeholder": "Hasło",
                "id": "password",
            }
        )
    )


class VoteForm(forms.ModelForm):
    """Form definition for Vote."""

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-controls", "id": "some_id"}),
    )

    class Meta:
        """Meta definition for Voteform."""

        model = Vote
        fields = ("name",)


class VoteForm(forms.ModelForm):
    """Form definition for Vote."""

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-controls", "id": "some_id"}),
    )

    class Meta:
        """Meta definition for Voteform."""

        model = Vote
        fields = ("name",)


class NewUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "username",
                "class": "form-control input-sm",
                "placeholder": "Nazwa Użytkownika",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "name": "email",
                "class": "form-control input-sm",
                "placeholder": "Adres Email",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "name": "password",
                "class": "form-control input-sm",
                "placeholder": "Hasło",
                "id": "password",
            }
        ),
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "name": "password_confirmation",
                "class": "form-control input-sm",
                "placeholder": "Potwierdź Hasło",
                "id": "password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):

    body = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "body",
                "class": "form-control input-sm",
                "placeholder": "Tytuł Wydarzenia",
            }
        ),
    )

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ("body", "created_on", "kolejka")

    def clean_tank(self):
        if not self["kolejka"].html_name in self.data:
            return self.fields["kolejka"].initial
        return self.cleaned_data["kolejka"]


class KolejkaForm(forms.ModelForm):
    class Meta:
        model = Kolejka
        fields = "__all__"
