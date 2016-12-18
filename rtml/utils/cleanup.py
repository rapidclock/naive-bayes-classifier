import os
import re
import string

class CleanUp():
	"""
	Cleans up a list of strings with the given options selected.
	"""
	def __init__(self, input, tokenize=True, url=True, punct=True, lower=True, stopwords=True):
		self.original = input[:]
		self.output = []
		self.tokenize = tokenize
		self.stopwords = stopwords
		self.func_chain = []
		if url:
			self.func_chain.append(self.__url_filter)
		if punct:
			self.func_chain.append(self.__punct_filter)
		if lower:
			self.func_chain.append(self.__lower_sweep)
		if self.stopwords:
			self.__build_stop_words_db()
			self.func_chain.append(self.__filter_stop_words)
		
	def __build_stop_words_db(self, stop_word_file='stopwords.txt'):
		self.stopword_dict = {}
		try:
			script_dir = os.path.dirname(__file__)
			file = open(script_dir+'/'+stop_word_file)
			for word in file:
				str = word.strip()
				self.stopword_dict[str] = None
		except IOError:
			print 'stopword file not found'
	
	def __filter_stop_words(self, inp_list):
		temp_store = []
		for sentence in inp_list:
			tokenized = sentence.split()
			clean_list = []
			for token in tokenized:
				if not self.stopword_dict.has_key(token):
					clean_list.append(token)
			if self.tokenize:
				temp_store.append(clean_list)
			else:
				str = reduce(lambda x, y: x+' '+y, clean_list)
				temp_store.append(str)
		return temp_store

	def __url_filter(self, inp_list):
		local_store = []
		for sentence in inp_list:
			result = re.sub(r"http\S+", "", sentence)
			local_store.append(result)
		return local_store

	def __punct_filter(self, inp_list):
		local_store = []
		for sentence in inp_list:
			result = sentence.translate(None, string.punctuation)
			local_store.append(result)
		return local_store

	def __lower_sweep(self, inp_list):
		local_store = []
		for sentence in inp_list:
			result = sentence.lower()
			local_store.append(result)
		return local_store

	def process(self):
		self.output = self.original[:]
		for func in self.func_chain:
			self.output = func(self.output)
		return self.output[:]