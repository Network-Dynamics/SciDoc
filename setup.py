import sys
import os

if sys.argv[1]=='--configure':
	handlers_file=sys.argv[2]
	
	f=open(handlers_file,'r')
	inifile=open("handlers/__init__.py",'w')

	handlerdict={}

	for line in f.readlines():
		if not line.isspace():
			handlername, handlerfile=line.split()
			handlerdict[handlername]=os.path.basename(handlerfile)
	
	
	print >> inifile, "__all__=",handlerdict.values()
	
	for handlerf in handlerdict.itervalues():
		print>> inifile, "import ",handlerf
	

	print >> inifile, "handlermap={}"
	for key,val in handlerdict.iteritems():
		print >> inifile, "handlermap['%s']=%s.handler"%(key,val)


