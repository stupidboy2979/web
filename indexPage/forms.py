from django import forms
from .models import Company
class newCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'portal', 'dpc', 'remarks', 'created_by']