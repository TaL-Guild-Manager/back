import dataclasses

from django import forms
from .models import Grade


class GradeForm(forms.ModelForm):

    @dataclasses.dataclass
    class Meta:
        model = Grade
        fields = (
            'label',
        )