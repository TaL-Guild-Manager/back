import dataclasses

from django import forms
from .models import CombatType


class CombatTypeForm(forms.ModelForm):

    @dataclasses.dataclass
    class Meta:
        model = CombatType
        fields = (
            'label',
        )