from django import forms
from .models import Temp

class temp_form(forms.ModelForm):
    class Meta:
        model = Temp
        fields = [
            "amp"
        ]