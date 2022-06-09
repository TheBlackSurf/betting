from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VoteForm(forms.ModelForm):
    """Form definition for Vote."""
    name = forms.CharField(max_length=100,
                            widget= forms.TextInput
                            (attrs={'class':'form-controls',
                    'id':'some_id'}))
    class Meta:
        """Meta definition for Voteform."""

        model = Vote
        fields = ('name',)
        
        
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user