from django import forms
from apps.profileUser.models import ProfileUser


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = (
            'user',
            'theme_dark',
        )
        exclude = ('active','dt_created',)
