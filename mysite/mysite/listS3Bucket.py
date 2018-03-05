#!/usr/bin/env python

import boto3

# Get the service client
s3 = boto3.resource('s3')

bucket = s3.Bucket('xinkaibuk1')
keys=bucket.objects.all()
for key in keys:
	print key.key
