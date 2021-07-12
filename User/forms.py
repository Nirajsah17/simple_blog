from django import forms
from .models import blog

class postform(forms.ModelForm):
	class Meta :
		model = blog
		fields=['text']