from django import forms
from .models import joinsquad

class joinsquadform(forms.ModelForm):
    class Meta:
        model = joinsquad
        fields = [
            'gamername',
            'fullname',
            'playerid',
        ]
