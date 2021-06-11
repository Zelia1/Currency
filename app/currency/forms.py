from django import forms

from currency.models import Banks

class BankForm(forms.ModelForm):
	class Meta:
		model = Banks
		fields = (
			'name',
			'url',
			'email_from',
			'number_phone',
		)