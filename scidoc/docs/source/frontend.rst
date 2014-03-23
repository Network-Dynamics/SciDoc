.. include global.rst
:program:`check_document.py` --- improve bad documents
******************************************************
:program:`check_document.py` has a in-built help which can be accessed by running on the terminal::

   python text-analyze.py
    
Which produces this output::

   usage: check_document.py [-h] [-t TYPE] textfile configfile
   check_document.py parses a document, analyzes it using user-definable rules, and
   presents the user with the results

   positional arguments:
     textfile              The path to the file to analyze
     configfile            The path to the configuration file listing handlers to
                           apply

   optional arguments:
     -h, --help            show this help message and exit
     -t TYPE, --type TYPE  format of textfile, valid options: txt/tex
   

Here's a basic example of running the program :program:`text-analyze.py` on a text file located at :file:`texts/thesis.txt` with the rules (henceforth called 'handlers') specified in the configfile :file:`sample.conf`::

   python text-analyze.py texts/thesis.txt sample.conf 

This produces the output::
   
   {'nparas': 1060, 'nwords': 19143, 'nsents': 2073}
   You have used these variations of the same word: Fig,Figure. Consider using only one.

We describe how to write config files in the next section.

Writing your own configfile
----------------------------

A configfile is a plaintext file with one or more columns in each line. Blank lines are ignored. Columns are separated by a single tab. The first column mentions the name of the rule to apply. The rest of the columns specify the arguments the rule accepts. Here is a barebones configfile::

   stat
   variation_detect        "list"  [("Fig", "Figure")]

The first line specifies that the handler named ``stat`` will be applied with no additional arguments. 
The secodn line specifies that the handler named ``variation_detect`` will be applied with additional arguments ``"list"`` and ``[("Fig", "Figure")]``. 

To write your own configfile, you therefore need to know:

1. Which handlers are avilable to you.
2. Which arguments need to be supplied to each handler. 

This information should be supplied by the developers writing the handlers. 

.. note:: Will add link to the handler doc page

