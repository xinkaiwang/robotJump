# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from models import *

# Create your views here.

def buckets(request):
	return render(request, 'buckets/index.html', {'title':'Bucket列表', 'bucket_list':BucketInfo.objects.all()})

def bucketDetails(request, id):
	images = BucketInfo.objects.get(id=id).imageinfo_set.all();
	return render(request, 'buckets/bucketDetail.html', {'title':'Bucket内容', 'image_list':images})
