from django.conf.urls import url,include

from django.contrib.auth import views
from .import views

urlpatterns = [
# post views
	#url(r'^login/$', views.user_login, name='login'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^register/$', views.register, name='register'),
	url('^', include('django.contrib.auth.urls')),
	
]