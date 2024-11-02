from django import forms
from .models import Roadster


class RoadsterForm(forms.ModelForm):

    class Meta:
        model = Roadster
        fields = (
            'label',
            'is_pvp',
            'members',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            instance.save()
            if 'members' in self.cleaned_data:
                instance.members.set(self.cleaned_data['members'])
        return instance