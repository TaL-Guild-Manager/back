from django import forms
from .models import Loot


class LootForm(forms.ModelForm):
    class Meta:
        model = Loot
        fields = (
            'label',
            'boss',
            'loot_type',
        )
