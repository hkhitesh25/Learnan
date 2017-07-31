# /-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from account import models
from .models import Stream,Question
# Create your views here.

def question_list(request,stream_slug=None):
	
	stream=None
	streams=Stream.objects.all()
	questions=Question.objects.filter(available=True)
	if stream_slug:
		stream=get_object_or_404(Stream,slug=stream_slug)
		questions= questions.filter(stream=stream)
	return render(request,'test_questions/list.html',{'stream': stream,
													'streams': streams,
													'questions': questions})
	
	
def question_detail(request,id,slug):
	question= get_object_or_404(Question,id=id,slug=slug,available=True)
	return render(request,'test_questions/detail.html',{'question': question})



