:mod:`text-analyze` --- Text analyzer for scientific documents
===============================================================
.. automodule:: scidoc
   :synopsis: A simple text parser that analyzes scientific documents according to user-configurable rules (handlers) .

Submodule -- auto members
=========================

.. automodule:: scidoc.handlers

-------------------------
This module defines functions for parsing a documents in various formats (currently supported: plaintext and latex) using NLTK ?? and detecting prevalent bad writing styles.          					


Example code
------------
:mod:`text-analyze.py` has a in-built help which can be accessed by running on the terminal:
   python text-analyze.py 
Which produces this output:

   usage: text-analyze.py [-h] [-t TYPE] textfile configfile
   text-analyze.py: error: too few arguments
   dmanik@chao ~/scidoc $ python text-analyze.py -h
   usage: text-analyze.py [-h] [-t TYPE] textfile configfile
   
   text-analyze parses a document, analyzes it using user-definable rules, and
   presents the user with the results
   
   positional arguments:
     textfile              The path to the file to analyze
     configfile            The path to the configuration file listing handlers to
                           apply
   
   optional arguments:
     -h, --help            show this help message and exit
     -t TYPE, --type TYPE  format of textfile, valid options: txt/tex
   

Here's a basic example of running the program :program:`text-analyze.py` on a text file located at :file:`texts/thesis.txt` with the rules (henceforth called 'handlers') specified in the configfile :file:`sample.conf`.

   python text-analyze.py texts/thesis.txt sample.conf 

This produces the output:
   
   {'nparas': 1060, 'nwords': 19143, 'nsents': 2073}
   You have used these variations of the same word: Fig,Figure. Consider using only one.

How to write config files are described in the next section.

Writing your own configfile
----------------------------

A configfile is a plaintext file with one or more columns in each line. Blank lines are ignored. Columns are separated by a single tab. The first column mentions the name of the rule to apply. The rest of the columns specify the arguments the rule accepts. Here is a barebones configfile:

   stat
   variation_detect        "list"  [("Fig", "Figure")]

The first line specifies that the handler named 'stat' will be applied with no additional arguments. 
The secodn line specifies that the handler named 'variation_detect' will be applied with additional arguments "list" and [("Fig", "Figure")]. 

To write your own configfile, you therefore need to know:
1. Which handlers are avilable to you.
2. Which arguments need to be supplied to each handler. 

This information should be supplied by the developers writing the handlers. 

Writing/adding a new handler
----------------------------
Each handler must be a python function that accepts a *nltk.corpus.PlaintextCorpusReader* object (http://nltk.googlecode.com/svn/trunk/doc/api/nltk.corpus.reader.plaintext.PlaintextCorpusReader-class.html) as its first argument. It can accept any number of other arguments. 

For example, the source code for the statistics handler is provided below:

    def handler(text):
        return {'nwords':len(text.words()),'nsents':len(text.sents()),'nparas':len(text.paras())}


