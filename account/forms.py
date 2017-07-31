from django.contrib.auth.models import User
from django import forms
from .models import Profile



class UserRegistrationForm(forms.ModelForm):

    
    							
	password = forms.CharField(label='Password',
								widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password Again',
								widget=forms.PasswordInput)
	#stream = forms.ChoiceField(choices=CHOICES, required=True, label='Stream')
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')
CHOICES = (('IIT-JEE', 'IIT-JEE'),('Medical','Medical'),('Commerce','Commerce'))

class ProfileForm(forms.ModelForm):
	
    stream= forms.ChoiceField(choices=CHOICES, required=True, label='Stream')

    class Meta:
        model = Profile
        fields = ('stream',)

def clean_password2(self):
	cd = self.cleaned_data
	if cd['password'] != cd['password2']:
		raise forms.ValidationError('Passwords don\'t match.')
	return cd['password2']
class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)