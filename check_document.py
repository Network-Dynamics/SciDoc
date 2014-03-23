import argparse
import scidoc


main_doc="""text-analyze parses a document, analyzes it using user-definable rules, and presents the user with the results"""

parser = argparse.ArgumentParser(description=main_doc)
parser.add_argument('textfile',help="The path to the file to analyze")
parser.add_argument('configfile',help="The path to the configuration file listing handlers to apply")
parser.add_argument("-t","--type", help="format of textfile, valid options: txt/tex")

try:
	args=parser.parse_args()
	if args.type:
		doctype=args.type
	else:
		doctype='txt'	
	scidoc.text_analyze(args.textfile,args.configfile,doctype)
except Exception, e :
	print e
		
