from django import forms

from . import models

class CreatePersoneForm(forms.ModelForm):
	phones = forms.CharField(widget=forms.TextInput, max_length=50)
	class Meta:
		model = models.Persone
		fields = (
			'name',
			'division',
			'phones'
		)