from handlers import *
import os

#handlermap={'stat':statistics_handler, 'variation_detect':variation_detect_handler}



def read_conf(config):
	"""
	Will parse the file named config and tell us which handlers to use
	"""
	f=open(config,'r')
	conflines=f.read().strip().split('\n')
	

	res=[]

	for confline in conflines:
		fields=confline.split('\t')
		handler=handlermap[fields[0]]
		
		if len(fields)>1:
			paramlist=[]

			for detail in fields[1:]:
				paramlist.append(eval(detail))
	
			res.append((handler,tuple(paramlist)))
		else:
			res.append((handler,()))	

	f.close()
	return res

def ui_handler(output):
	"""
	this will take care of interacting with the user
	"""
	print output




def apply_rules(text,config):		#must be passed an NLTK corpus and a config file
	parsed_config=read_conf(config)

	for handler,params in parsed_config:
		output=handler(text,*params)
		ui_handler(output)


def parse_raw(source,typ='txt'):
	"""
	parses docuemnts of different formats and returns an NLTK corpus
	"""
	corpus_root=os.path.dirname(source)
	filename=os.path.basename(source)

	return nltk.corpus.PlaintextCorpusReader(corpus_root, filename)	#loads all files w/ name ending in txt



if __name__=='__main__':
	import nltk.corpus
	text=parse_raw("./texts/thesis.txt")
	apply_rules(text,"sample.conf")


