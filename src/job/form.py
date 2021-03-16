from django import forms

from .models import apply, job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name', 'email', 'website', 'cv', 'cove_letter']


class AddForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('owner', 'slug',)
