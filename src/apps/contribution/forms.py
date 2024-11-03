from django import forms
from .models import Contribution


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = (
            'member',
            'start',
            'end',
            'contribution_start',
            'contribution_end'
        )
