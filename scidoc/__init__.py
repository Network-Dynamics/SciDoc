#__all__=['text-analyze']

""" 
.. moduleauthor:: Debsankha Manik <dmanik@nld.ds.mpg.de>

This module contains a bunch of functions that helps you analyze scientific documents according to user-configurable rules (handlers). 
"""

#import sys
#sys.path.append("./")

import handlers
from handlers import *
import os, commands
import nltk.corpus



def _read_conf(config):
	"""
	Will parse the file named config and tell us which handlers to use
	"""
	f=open(config,'r')
	conflines=f.readlines()
	
	res=[]

	for confline in conflines:
		if confline.isspace():
			continue
		fields=confline.strip().split('\t')	#fields[0]==handlername, fields[1:] are parameters, vald python expressions
		handler=handlers.handlermap[fields[0]]
		
		if len(fields)>1:
			paramlist=[]

			for detail in fields[1:]:
				paramlist.append(eval(detail))
	
			res.append((handler,tuple(paramlist)))
		else:	#a handler without any parameters
			res.append((handler,()))	
	f.close()
	return res

def ui_hook(output):
	"""
	this will take care of interacting with the user
	"""
	print output




def _apply_rules(text,config):		#must be passed an NLTK corpus and a config file listing which handler to use
	parsed_config=_read_conf(config)

	for handler,params in parsed_config:
		output=handler(text,*params)
		ui_hook(output)


def parse_raw(source,typ='txt'):
	"""
	parses docuemnts of different formats and returns an NLTK corpus
	"""
	corpus_root=os.path.dirname(source)
	filename=os.path.basename(source)
	if typ=='txt':
		return nltk.corpus.PlaintextCorpusReader(corpus_root, filename)	
	elif typ=='tex':
#Needs detex to be installed, assumes I/O redirection works
		txtfilename=filename+".txt"
		commands.getoutput("detex %s/%s > %s/%s"%(corpus_root,filename,corpus_root,txtfilename))
		return nltk.corpus.PlaintextCorpusReader(corpus_root, txtfilename)	
	else:
		pass
			
def text_analyze(path,handlerconf,doctype):
	"""analyzes a file according to rules specified. Displays suggestion in a user-friendly way
	
	Args:
		path: path to the document to be analyzed
		handlerconf:  oath to a configfile listing which rules to apply
		doctype: Type of document. Currently supported: txt/tex
	
	Returns:
		None
		Output is piped to a suitable the function ``ui_hook``
		
	"""
	text=parse_raw(path, typ=doctype)
	_apply_rules(text,handlerconf)



