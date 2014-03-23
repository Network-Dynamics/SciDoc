import sys
import os,commands

docstr="""
scidoc.handlers module
=======================
This module consists of all the handlers, i.e. semantic rules to be applied to a scientific document. 

How to write handlers
---------------------
Each handler resides in its own file :file:`scidoc/handlers/<handlername.py>`. 
Each :file:`scidoc/handlers/<handlername.py>` must define a function named :func:`apply` that accepts a :class:`nltk.corpus.PlaintextCorpusReader` object (http://nltk.googlecode.com/svn/trunk/doc/api/nltk.corpus.reader.plaintext.PlaintextCorpusReader-class.html) as its first argument. It can accept any number of other arguments. 



``handlername.py`` must have a function 
:func:`handle` that does fairy tales. 

"""


if sys.argv[1]=='--configure':
	f=open('handlers.list','r')
	inifile=open("handlers/__init__.py",'w')
	print >>inifile, '"""%s"""'%docstr
	print
	handlerdict={}

	for line in f.readlines():
		if not line.isspace():
			handlername, handlerfile=line.split()
			handlerdict[handlername]=os.path.basename(handlerfile)
	
	f.close()
		
	print >> inifile, "__all__=",handlerdict.values()
	
	for handlerf in handlerdict.itervalues():
		print>> inifile, "import ",handlerf
	

	print >> inifile, "handlermap={}"
	for key,val in handlerdict.iteritems():
		print >> inifile, "handlermap['%s']=%s.apply"%(key,val)
	
	os.chdir(sys.path[0]+'/docs')
	print commands.getoutput("make html")
