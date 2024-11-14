from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    vaquero_id = forms.CharField(max_length=100, label="Vaquero ID")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'vaquero_id']  # Include Vaquero ID

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        # Create the Profile and save the Vaquero ID
        profile = Profile.objects.create(user=user, vaquero_id=self.cleaned_data['vaquero_id'])
        profile.save()

        return user
