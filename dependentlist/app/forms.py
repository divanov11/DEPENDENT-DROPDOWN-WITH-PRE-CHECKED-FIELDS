from django import forms
from django.forms import ModelForm
from .models import *

class SifForm(forms.ModelForm):
	class Meta:
		model = Sample
		fields = '__all__'
		exclude = ['tests']
