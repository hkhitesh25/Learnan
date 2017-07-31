# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,ProfileForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm,ProfileForm
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.db import transaction

# Create your views here.

def index(request):
	return render(request,
				'account/index.html',
				)	



#def user_login(request):
#	if request.method=='Post':
#		form=LoginForm(request.Post)
#		if form.is_valid:
#			cd=form.cleaned_data
#			user=authenticate(username=cd['username'],password=cd['password'])
#			if user is not None:
#				if user.is_active:
#					login(request,user)
#					return HttpResponse('Authenticated '\
#										'successfully')
#											
#				else :
#					return HttpResponse("Disabled account")
#		else :
#			return HttpResponse("Invalid Login")
#	else:
#		form=LoginForm()
#		return render(request,'account/login.html', {'form': form})			

@transaction.atomic

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			#new_user = profile_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(
				user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			login(request,new_user)
							
			return render(request, 'account/index.html' )
	else:
		user_form = UserRegistrationForm()
	
	return render(request,
				'account/register.html',
				{'user_form': user_form})
@login_required
def profile(request):
	if request.method == 'POST':
		profile_form = ProfileForm(request.POST, instance=request.user.profile)

		if profile_form.is_valid():
			profile_form.save()
			return render(request, 'account/index.html', {})
	else:		
		profile_form = ProfileForm(instance=request.user.profile)
		return render(request,
				'account/profile.html',
				{'profile_form': profile_form})