#!/usr/bin/env python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

# your imports, e.g. Django models
from buckets.models import *

all = ImageInfo.objects.all()

for b in all:
	print b
