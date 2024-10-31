import dataclasses

from django import forms
from .models import Member


class MemberForm(forms.ModelForm):

    @dataclasses.dataclass
    class Meta:
        model = Member
        fields = (
            'username',
            'added_at',
            'is_on_discord',
            'is_active',
            'is_pvp',
            'has_privilege',
            'grade',
            'weapon',
            'combat_type',
        )