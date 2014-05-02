from .. import shift, substitution
from .. import alphabet
#~ from cipher2 import ciphertext
from test_shift_cipher import ciphertext, alphabet
import dictionary

_max = 0

for k in xrange(len(alphabet)):
	print "Attempting with key:", k
	try:
		message = shift.decrypt(k, ciphertext, alphabet)
		found = dictionary.word_count(message)
		#~ print message
		if found > _max:
			_max = found
			_maxkey = k
			
	except Exception as e:
		print "Failed:", e
	#~ s = raw_input("Continue?")
	
print " DONE! "
print
print
print "Most likely from dictionary"
message = shift.decrypt(_maxkey, ciphertext, alphabet)
print message
print "Number of words found from dictionary: ", _max
print "Key:", _maxkey
