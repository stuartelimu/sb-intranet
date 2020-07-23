from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

User = get_user_model()


class RegistrationForm(UserCreationForm):

    TEAM_CHOICES = (
        ('IB', 'INBOUND'),
        ('OB', 'OUTBOUND'),
        ('WI', 'WALK IN'),
        ('FD', 'FOOD'),
        ('SM', 'SOCIAL MEDIA'),
        ('OT', 'OTHER')
    )

    team = forms.ChoiceField(choices=TEAM_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'team',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('team', 'avatar')
