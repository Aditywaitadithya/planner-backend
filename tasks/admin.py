# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import customer, taskDetails, joiningTask
from django.contrib import admin


class TaskAdmin(admin.ModelAdmin):
    model = taskDetails
    filter_horizontal = ('customersInvolved',)

# Register your models here.

admin.site.register(customer)
admin.site.register(taskDetails, TaskAdmin)
admin.site.register(joiningTask)
