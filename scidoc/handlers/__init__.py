"""
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
__all__= ['statistics', 'variation_detect']
import  statistics
import  variation_detect
handlermap={}
handlermap['stat']=statistics.apply
handlermap['variation_detect']=variation_detect.apply
