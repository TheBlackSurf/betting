from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from .models import *


class RFPAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control input-sm", "placeholder": "Nazwa Użytkownika"})
    )
    password = forms.CharField(
        widget=PasswordInput( attrs={
                "type": "password",
                "name": "password",
                "class": "form-control input-sm",
                "placeholder": "Hasło",
                "id": "password",
            })
    )


class VoteForm(forms.ModelForm):
    """Form definition for Vote."""

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-controls", "id": "some_id"}),
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
    # kolejka = forms.CharField(
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "type": "text",
    #                 "name": "body",
    #                 "class": "form-control input-sm",
    #                 "placeholder": "Kolejka",
    #             }
    #         ),
    #     )
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
    # created_on = forms.CharField(required=True,  widget= forms.TextInput(attrs={'type':'text', 'name':'email', 'class':'form-control input-sm', 'placeholder':'Data'}))

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ("body", "created_on", "kolejka")
    def clean_tank(self):
            if not self['kolejka'].html_name in self.data:
                return self.fields['kolejka'].initial
            return self.cleaned_data['kolejka']
        
class KolejkaForm(forms.ModelForm):
    
    class Meta:
        model = Kolejka
        fields = ('__all__')
