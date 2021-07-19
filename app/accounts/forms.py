import uuid

from django.conf import settings
from accounts.tasks import send_registration_email

from django import forms

from accounts.models import User


class SignUpForm(forms.ModelForm):
    password_one = forms.CharField()
    password_two = forms.CharField()

    class Meta:
        model = User
        fields = ('email', 'password_one', 'password_two')

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password_one'] != cleaned_data['password_two']:
                raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.username = str(uuid.uuid4())
        instance.is_active = False

        if commit:
            instance.save()

        body = f"""
        Activate your account
        {settings.DOMAIN}/activate/dsadsa-asd
        """

        send_registration_email.delay('TODO', self.cleaned_data['email'])

        return instance
