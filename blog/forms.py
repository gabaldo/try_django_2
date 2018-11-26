from django import forms

from .models import Article


class ArticleModelForm(forms.ModelForm):
	
	title = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'placeholder': 'Blog title',
			'class': 'form-control',
			}
			)
		)

	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
			'placeholder': 'Content',
			'class': 'form-control',
			'rows': 5,
			}
			)
		)

	active = forms.BooleanField(
		widget=	forms.CheckboxInput(attrs={'class': 'form-check-input'}),
		)

	class Meta:
		model = Article
		fields = [
			'title',
			'content',
			'active',
		]