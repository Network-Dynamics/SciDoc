def handler(text):
	return {'nwords':len(text.words()),'nsents':len(text.sents()),'nparas':len(text.paras())}


