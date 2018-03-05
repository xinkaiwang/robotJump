#!/usr/bin/env python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

# your imports, e.g. Django models
from buckets.models import *
from buckets.name2date import name2date

bucket = BucketInfo.objects.get(name='xinkaibuk1')

allInDb = set()
allInDb.update(ImageInfo.objects.all())

file_name='20180227.062043.749.jpg'
date = name2date(file_name)
# print date
img = ImageInfo(file_name=file_name, date_time=date, bucket=bucket)
img.save()

print 'image saved'