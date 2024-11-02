from django import forms
from .models import Blacklist


class BlacklistForm(forms.ModelForm):
    class Meta:
        model = Blacklist
        fields = (
            'username',
            'previous_guild',
            'reason',
        )