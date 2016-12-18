


def _RELIC__word_list_prep():
	file = open('stopwords.txt')
	new_file = open('stopwords_new.txt', 'w')
	for line in file:
		if line.strip():
			new_file.write(line)
	file.close()
	new_file.close()
