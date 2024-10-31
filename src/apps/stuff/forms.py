import dataclasses

from django import forms
from .models import Stuff


class StuffForm(forms.ModelForm):

    @dataclasses.dataclass
    class Meta:
        model = Stuff
        fields = (
            'label',
            'is_raid_loot',
            'loot_type',
            'boss',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.is_raid_loot:
            self.fields.pop('boss')