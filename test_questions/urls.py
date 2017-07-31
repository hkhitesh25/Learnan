from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^list/$',views.question_list,name='question_list'),
	url(r'^(?P<stream_slug>[-\w]+)/$',views.question_list,name='question_list_by_stream'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.question_detail,name='question_detail'),								
										
]