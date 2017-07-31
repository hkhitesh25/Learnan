# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.


class Stream(models.Model):
	name=models.CharField(max_length=200,db_index=True)
	slug=models.SlugField(max_length=200,db_index=True,unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'stream'
		verbose_name_plural = 'streams'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('test_questions:question_list_by_stream',args=[self.slug])


class Question(models.Model):
	stream=models.ForeignKey(Stream,related_name='questions')
	name=models.CharField(max_length=200,db_index=True)
	slug=models.CharField(max_length=200,db_index=True)
	image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
	description=models.TextField(blank=True)
	#price=models.DecimalField(max_digits=10,decimal_places=2)
	#stock=models.PositiveIntegerField()
	available=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together=(('id','slug'),)

	def __str__(self):
		return self.name		

	def get_absolute_url(self):
		return reverse('test_questions:question_detail',args=[self.id, self.slug])
#FRESHMAN = 'FR'
#SOPHOMORE = 'SO'
#JUNIOR = 'JR'
#SENIOR = 'SR'
#
#QUESTION_CHOICES = (
#        (FRESHMAN, 'Freshman',),
#        (SOPHOMORE, 'Sophomore'),
#        (JUNIOR, 'Junior'),
#        (SENIOR, 'Senior'),
#    )
class Choice(models.Model):
	
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,)
    

