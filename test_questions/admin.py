# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Stream,Question,Choice
# Register your models here.

class StreamAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Stream,StreamAdmin)

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['name','stream' ,'slug','available','created','updated']
	list_filter = ['available','created','updated','stream']
	list_editable = ['available']
	prepopulated_fields = {'slug' :('name',)}
admin.site.register(Question,QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ['question', 'choice_text','get_stream']

	def get_stream(self, instance):
		return instance.question.stream
	get_stream.short_description = 'Stream'
    
	#prepopulated_fields = {'slug':('name',)}
admin.site.register(Choice,ChoiceAdmin)