from django import forms
from .models import VisitForm


class VisitForm(forms.ModelForm):
    class Meta:
        model = VisitForm
        fields = '__all__'