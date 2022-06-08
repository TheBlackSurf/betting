from django import forms 
from .models import *


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
     