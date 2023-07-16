from django import forms
from .models import JSONFile
import json
from django.core.exceptions import ValidationError

class SubfolderForm(forms.Form):
    name = forms.CharField(max_length=100)

class JSONFileForm(forms.ModelForm):
    class Meta:
        model = JSONFile
        fields = ['name', 'content']
    
    #json validation of input file data
    def clean_content(self):
        content = self.cleaned_data['content']
        try:
            json.loads(content)
        except ValueError:
            raise ValidationError("Invalid JSON format")
        return content
