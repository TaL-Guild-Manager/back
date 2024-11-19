from django import forms
from django.core.exceptions import ValidationError
from .models import Stuff

class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = (
            'label',
            'is_raid_loot',
            'has_been_acquired',
            'acquired_at',
            'loot',
            'loot_type',
            'boss',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'initial' in kwargs:
            initial = kwargs['initial']
            is_raid_loot = initial.get('is_raid_loot', True)
        else:
            is_raid_loot = self.instance.is_raid_loot if self.instance.pk else True

        if not is_raid_loot:
            self.fields.pop('boss')

    def clean(self):
        cleaned_data = super().clean()
        is_raid_loot = cleaned_data.get('is_raid_loot')
        loot = cleaned_data.get('loot')
        boss = cleaned_data.get('boss')

        if is_raid_loot:
            if not loot:
                self.add_error('loot', 'Loot field is required when is_raid_loot is set to True.')
            else:
                cleaned_data['label'] = loot.label
                cleaned_data['loot_type'] = loot.loot_type

            if not boss:
                self.add_error('boss', 'Boss field is required when is_raid_loot is set to True.')
        else:
            cleaned_data.pop('boss', None)

        return cleaned_data
