from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Clinic

from . import MAX_STEPS, MAX_INGREDIENTS, CATEGORY, DIETARYREQ, ACC_TYPES

class newRecipeForm(forms.Form):
	recipe_title = forms.CharField(label='Recipe Title', max_length=50)
	recipe_category = forms.ChoiceField(choices=CATEGORY, widget=forms.RadioSelect())
	recipe_diet_req = forms.ChoiceField(choices=DIETARYREQ, required=False, widget=forms.RadioSelect())
	recipe_servings = forms.IntegerField(min_value=1, max_value=1000)
	recipe_duration = forms.IntegerField(min_value=1, max_value=20160)
	recipe_image = forms.ImageField()


	def __init__(self, *args, **kwargs):
		super(newRecipeForm, self).__init__(*args, **kwargs)

		for i in range(MAX_STEPS):
			self.fields['step_'+str(i)] = forms.CharField(label='Step '+str(i + 1), max_length=1024)

		for i in range(MAX_INGREDIENTS):
			self.fields['ingredient_'+str(i)] = forms.CharField(label='Ingredient '+str(i + 1), max_length=50)
			self.fields['iquantity_'+str(i)] = forms.CharField(label='Quantity '+str(i + 1), max_length=25)

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	account_type = forms.ChoiceField(choices=ACC_TYPES, widget=forms.RadioSelect())
	clinic = forms.ModelChoiceField(queryset=Clinic.objects.all().order_by('name'))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'clinic')
