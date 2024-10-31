import dataclasses

from django import forms
from .models import LootType


class LootTypeForm(forms.ModelForm):

    @dataclasses.dataclass
    class Meta:
        model = LootType
        fields = (
            'label',
        )