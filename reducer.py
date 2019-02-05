#!/usr/bin/python2
import sys
a=0
b=0
c=0
d=0
e=0
f=0
for x in sys.stdin:
	if "1" in x:
		a+=1
	if "2" in x:
		b+=1
	if "3" in x:
		c+=1
	if "4" in x:
		d+=1
	if "5" in x:
		e+=1
	if "6" in x:
		f+=1
print "1	{}".format(a)
print "2	{}".format(b)
print "3	{}".format(c)
print "4	{}".format(d)
print "5	{}".format(e)
print "6	{}".format(f)

