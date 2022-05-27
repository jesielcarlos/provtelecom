from django import forms
from apps.profileUser.models import ProfileUser


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = (
            'service_plan',
            'email',
            'city',
            'district',
            'address',
            'number',
            'cep'
        )
        exclude = ('active','dt_created',)
