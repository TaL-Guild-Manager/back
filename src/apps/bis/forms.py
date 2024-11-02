from django import forms
from .models import BiS


class BiSForm(forms.ModelForm):
    class Meta:
        model = BiS
        fields = (
            'member',
            'stuffs',
            'is_primary',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            instance.save()
            if 'stuffs' in self.cleaned_data:
                instance.stuffs.set(self.cleaned_data['stuffs'])
        return instance