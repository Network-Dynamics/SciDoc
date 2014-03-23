def apply(corpus):
	"""
	analyzes statistical properties of a corpus.

	Args:
		corpus: a valid 


	"""
	return {'nwords':len(corpus.words()),'nsents':len(corpus.sents()),'nparas':len(corpus.paras())}


