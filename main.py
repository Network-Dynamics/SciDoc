import handlers
from handlers import *
import os, commands
import nltk.corpus

#handlermap={'stat':statistics_handler, 'variation_detect':variation_detect_handler}



def read_conf(config):
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

def ui_handler(output):
	"""
	this will take care of interacting with the user
	"""
	print output




def apply_rules(text,config):		#must be passed an NLTK corpus and a config file listing which handler to use
	parsed_config=read_conf(config)

	for handler,params in parsed_config:
		print params
		output=handler(text,*params)
		ui_handler(output)


def parse_raw(source,typ='txt'):
	"""
	parses docuemnts of different formats and returns an NLTK corpus
	"""
	corpus_root=os.path.dirname(source)
	filename=os.path.basename(source)
	print corpus_root, filename	
	if typ=='txt':
		return nltk.corpus.PlaintextCorpusReader(corpus_root, filename)	
	elif typ=='tex':
#Needs detex to be installed, assumes I/O redirection works
		txtfilename=filename+".txt"
		commands.getoutput("detex %s/%s > %s/%s"%(corpus_root,filename,corpus_root,txtfilename))
		return nltk.corpus.PlaintextCorpusReader(corpus_root, txtfilename)	
	else:
		pass
			

if __name__=='__main__':
#	text=parse_raw("./texts/thesis.txt",typ='txt')
	text=parse_raw("./texts/epjst1.tex",typ='tex')
	apply_rules(text,"sample.conf")


