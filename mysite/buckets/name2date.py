#!/usr/bin/env python

from datetime import datetime
from django.utils.dateparse import parse_datetime

# input 20180227.062043.748.jpg
# return date
def name2date(fileName):
	# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
	o = datetime.strptime(fileName[0:15], '%Y%m%d.%H%M%S')
	str = o.strftime("%Y-%m-%d %H:%M:%S")
	return parse_datetime(str + fileName[15:19] + '-08:00')

# datetime.strptime('20180227.062043', '%Y%m%d.%H%M%S',tzinfo=-0800)

if __name__ == '__main__':    
	print name2date('20180227.062043.748.jpg')

	