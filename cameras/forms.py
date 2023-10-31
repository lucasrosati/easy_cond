from django import forms
from .models import CamerasProfile

class CamerasProfileForm(forms.ModelForm):
    class Meta:
        model = CamerasProfile
        fields = ['numero', 'area', 'url']