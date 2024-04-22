from django import forms

from profile.models import Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'bio', 'location', 'image']
