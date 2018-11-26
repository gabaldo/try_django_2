from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
	
	title = forms.CharField(
		label='Title',
		widget=forms.TextInput(
			attrs={
			'placeholder': 'Your title',
			'class': 'form-control',
			}
			)
		)

	description = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
				'placeholder': 'Your description',
				'class': 'form-control',
				'rows': 5,

				}
			)
		)

	price = forms.DecimalField(
		initial=199.99,
		widget=	forms.NumberInput(attrs={'class': 'form-control'}),
		)

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		if not 'CFE' in title:
			raise forms.ValidationError('This is not a valid title')
		return title


class RawProductForm(forms.Form):
	title		= forms.CharField()
	description = forms.CharField()
	price		= forms.DecimalField()