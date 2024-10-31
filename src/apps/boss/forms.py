import dataclasses

from django import forms
from .models import Boss


class BossForm(forms.ModelForm):

    @dataclasses.dataclass
    class Meta:
        model = Boss
        fields = (
            'label',
        )