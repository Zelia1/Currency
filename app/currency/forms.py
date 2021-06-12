from currency.models import Banks, ContactUs

from django import forms


class BankForm(forms.ModelForm):
	class Meta: # noqa
		model = Banks # noqa
		fields = ( # noqa
			'name', # noqa
			'url', # noqa
			'email_from', # noqa
			'number_phone' # noqa
		) # noqa


class ContactUsForm(forms.ModelForm):
	class Meta: # noqa
		model = ContactUs # noqa
		fields = ( # noqa
			'email_from', # noqa
			'subject', # noqa
			'message' # noqa
		) # noqa
