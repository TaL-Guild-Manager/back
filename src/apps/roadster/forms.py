import dataclasses

from django import forms
from .models import Roadster


class RoadsterForm(forms.ModelForm):

    @dataclasses.dataclass
    class Meta:
        model = Roadster
        fields = (
            'label',
            'is_pvp',
        )