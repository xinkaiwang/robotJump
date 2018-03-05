# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *
# Register your models here.

class BucketInfoAdmin(admin.ModelAdmin):
	list_display = ['id','name','start_date','last_sync_date']

class ImageInfoAdmin(admin.ModelAdmin):
	list_display = ['id','file_name','date_time', 'bucket']

admin.site.register(BucketInfo, BucketInfoAdmin)
admin.site.register(ImageInfo, ImageInfoAdmin)
