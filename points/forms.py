from django import forms
from .models import ProfilePoint

class ProfilePointForm(forms.ModelForm):
    
    class Meta:
        model = ProfilePoint
        fields = ('__all__')
