# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email','get_stream', 'first_name', 'last_name', 'is_staff' )
    list_select_related = ('profile', )
    def get_stream(self, instance):
        return instance.profile.stream
    get_stream.short_description = 'Stream'
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
#from django.contrib.auth.models import User
#
## Register your models here.
#admin.site.unregister(User)
#class UserAdmin(admin.ModelAdmin):
#    list_display = ('email', 'first_name', 'last_name','stream')
#    list_filter = ('is_staff', 'is_superuser')
#
#
##admin.site.unregister(User)
#admin.site.register(User, UserAdmin)
#