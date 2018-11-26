from django import forms

from .models import Course


class CourseModelForm(forms.ModelForm):
	
	title = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'placeholder': 'Course title',
			'class': 'form-control',
			}
			)
		)


	class Meta:
		model = Course
		fields = [
			'title',
		]