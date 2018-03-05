# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BucketInfo(models.Model):
	name = models.CharField(max_length=20)
	start_date = models.DateTimeField()
	last_sync_date = models.DateTimeField()

	def __str__(self):
		return self.name.encode('utf-8')


class ImageInfo(models.Model):
	file_name = models.CharField(max_length=40)
	date_time = models.DateTimeField()
	bucket = models.ForeignKey(BucketInfo)

	def __str__(self):
		return self.file_name.encode('utf-8')
