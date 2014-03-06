def statistics_handler(text):
	return {'nwords':len(text.words()),'nsents':len(text.sents()),'nparas':len(text.paras())}


def variation_detect_handler(text,varlist):	#if many variations of same expression are used, suggests using one option only
	wds=text.words()
	for var in varlist:
		kinds=0
		for opt in var:
			if opt in wds:
				kinds+=1
		if kinds>1:
			return "You have used these variations of the same word: %s. Consider using only one."%(','.join(var))		

handlermap={'stat':statistics_handler, 'variation_detect':variation_detect_handler}
#this keys in handlermap must exactlymatch the names used in config files. and never place any rile after the handlermap declaration. it will cause KeyError
