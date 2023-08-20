from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Company"
    )
    field = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Field"
    )

    class Meta:
        model = Company
        fields = ['name', 'field']

    def clean_name(self):
        # Jika instance ada dan nama telah diubah
        if self.instance and self.instance.pk and 'name' in self.changed_data:
            raise forms.ValidationError('You cannot change the name field.')
        return self.cleaned_data['name']

