from django import forms
from .models import Distribution


class DistributionForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = (
            'loot',
            'members',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            instance.save()
            if 'members' in self.cleaned_data:
                instance.members.set(self.cleaned_data['members'])
        return instance