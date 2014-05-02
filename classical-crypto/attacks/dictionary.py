'''
Builds a dictionary using the linux /usr/share/dict/words file.
'''
english_words = set()
letter_counts = dict()
print "Loading dictionary..."
for line in file("/usr/share/dict/words"):
	line = line.replace('\n', '')
	english_words.add(line)
	for c in line:
		c = c.lower()
		if c in letter_counts.keys():
			letter_counts[c] = letter_counts[c] + 1
		else:
			letter_counts[c] = 0
	
letter_counts['_'] = 300000

def word_count(text, alphabet):
	count = 0
	splitted = text.split(alphabet.wordsplitter)
	for w in english_words:
		if w.upper() in splitted or w.lower() in splitted:
			count += 1
	return count
			
#~ print len(english_words)
#~ print letter_counts
