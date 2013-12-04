#!/usr/bin/python
from __future__ import division
import re

try:	
	import nltk.corpus
except ImportError:
	print "install python-nltk"	
	exit(1)

try:	
	import numpy as np
except ImportError:
	print "install python-numpy"	
	exit(1)

try:	
	import simplejson
except ImportError:
	print "install python-simplejson"	
	exit(1)

print "all modules have been installed"


corpus_root = './texts/'				#looks for text files in "./texts" directory
text=PlaintextCorpusReader(corpus_root, '.*txt')	#loads all files w/ name ending in txt



#class DocFixer:





def rule_sentlen(text,maxlimit):	#avg. length of sentences should be <threshold
	avgsenlength=len(text.words())/len(text.sents())
	return avgsenlength<maxlimit


def rule_commas(text,maxlimit):		#number of commas should not exceed threshold  
	allsents=text.sents()
	for sent in allsents:
		if sent.count(',')>maxlimit:
			print "More commas than %s in this sentence: %s"%(maxlimit, ' '.join(sent))
			print

def rule_variations(text,varlist):	#if many variations of same expression are used, suggests using one option only
	wds=text.words()
	for var in varlist:
		kinds=0
		for opt in var:
			if opt in wds:
				kinds+=1
		if kinds>1:
			print "You have used these variations of the same word: %s. Consider using only one."%(','.join(var))		
			print


def rule_wrong_context(text,word,context,alt):	#if word is used in context, suggests using alt
	sents=text.sents()
	for sent in sents:
		concat=' '.join(sent)
		if context in concat and word in concat:
			print "Consiver using \'%s\' instead of \'%s\' in this sentence: %s"%(alt,word,concat)


print "Average length of sentences is: %s"%("Ok" if rule_sentlen(text,12) else "too long")
print 
rule_commas(text,4)
rule_variations(text,[("Fig", "Figure")])
rule_wrong_context(text, 'Letter', 'Physical Review', 'Letters')



#
#{prl}
#sentence length<15
#abstract length<300


#output suggestion:
#line number/paragraph number
#errorcode

