import dataclasses

from django import forms
from .models import Weapon


class WeaponForm(forms.ModelForm):

    @dataclasses.dataclass
    class Meta:
        model = Weapon
        fields = (
            'label',
        )