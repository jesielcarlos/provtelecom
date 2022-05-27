from django import forms
from apps.callSystem.models import Called
from apps.profileUser.models import ProfileUser


class CalledForm(forms.ModelForm):
    class Meta:
        model = Called
        fields = (
            'title',
            'description'
        )
        exclude = ('active','dt_created','profile','situation')
