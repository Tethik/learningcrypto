from .. import substitution
from .. import alphabet
import dictionary

#~ from cipher1 import ciphertext, alphabet
#~ from test_shift_cipher import ciphertext, alphabet
#~ from cipher2 import ciphertext, alphabet
from test_sub_cipher import ciphertext, alphabet




letter_counts_ciphertext = dict()
for c in ciphertext:
	if c in letter_counts_ciphertext.keys():
		letter_counts_ciphertext[c] = letter_counts_ciphertext[c] + 1
	else:
		letter_counts_ciphertext[c] = 1
	
print dictionary.letter_counts
print letter_counts_ciphertext

def sort_valuation(c, c2, table):
	a = 0
	b = 0
	if c2 in table.keys():
		a = table[c2]
	if c in table.keys():
		b = table[c]
	return a - b
	
def cmp_cipher(c, c2):
	return sort_valuation(c, c2, letter_counts_ciphertext)
	
def cmp_dict(c, c2):
	if c == ' ':
		c = '_'
	if c2 == ' ':
		c2 = '_'
	return sort_valuation(c.lower(), c2.lower(), dictionary.letter_counts)


alphabetstr = sorted(alphabet.alphabetstr, cmp=cmp_cipher)
alphabetstr2 = sorted(alphabet.alphabetstr, cmp=cmp_dict)
print
print "Sorted strs:"
print "Cipher: ", alphabetstr
print
print "Dictionary: ", alphabetstr2

# Cracktiem
key = [alphabet.ord(alphabetstr[alphabetstr2.index(c)]) for c in alphabet.alphabetstr]
found = 0
threshold = 1000

while threshold > found:
	print 
	m = substitution.decrypt(key, ciphertext, alphabet)
	print m
	words = m.split(alphabet.wordsplitter)
	word_counts = dict()
	for w in words:
		if not w:
			continue
		if not w in word_counts.keys():
			word_counts[w] = 0
		word_counts[w] += 1
		
	def cmp_top(a,b):
		return sort_valuation(a,b,word_counts)
	
	top10words = [(w, word_counts[w]) for w in sorted(word_counts.keys(), cmp=cmp_top)][0:30]
		
	found = dictionary.word_count(m, alphabet)
	print top10words
	print found
	print "Key:",key
	print [alphabet.chr(k) for k in key]
	swap = raw_input("Swap?")
	if not swap:
		break
	parts = swap.split(" ")
	a = alphabet.ord(parts[0])
	b = alphabet.ord(parts[1])
	print parts, a, b
	key[a], key[b] = key[b], key[a]	
	for i in xrange(len(alphabet)):
		assert(i in key)
	print "Key:",key
	print [alphabet.chr(k) for k in key]
	swap = raw_input("Swap?")
	
	

