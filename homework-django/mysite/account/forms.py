from .models import Profile
from django import forms


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'name')

    def save(self, user=None):
        user_profile = super(EditProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile
