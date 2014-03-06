def handler(text,input_type,vars):	#if many variations of same expression are used, suggests using one option only
	wds=text.words()
	if input_type=='list':
		varlist=vars
	elif input_type=='file':
		f=open(vars,'r')
		lines=f.readlines()
		varlist=[tuple(i.strip().split('\t')) for i in lines]
		f.close()
	else:
		pass
			
	for var in varlist:
		kinds=0
		for opt in var:
			if opt in wds:
				kinds+=1
		if kinds>1:
			return "You have used these variations of the same word: %s. Consider using only one."%(','.join(var))		

