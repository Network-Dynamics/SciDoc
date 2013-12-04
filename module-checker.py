#!/usr/bin/python

modulelist=["nltk.corpus","numpy", "simplejson"]

for module in modulelist:
	try:
		exec("import %s"%module)
	except ImportError:
		print "Error: %s module is not found"%module	
		exit(1)
	
print "All modules are installed correctly"


