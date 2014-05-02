class Alphabet:	
	wordsplitter = ' '	
	def __init__(self, alphabetstr):
		self.alphabetstr = alphabetstr
		self.shortcut = dict()
		i = 0
		for c in alphabetstr:
			self.shortcut[c] = i
			i += 1
	
	def __unicode__(self):
		return self.alphabetstr
		
	def filter(self, inputstr):
		outputstr = ""
		for c in inputstr:
			if c in self.alphabetstr:
				outputstr += c
		return outputstr
		
	'''
	Encodes to vector of int.
	'''
	def encode(self, message):
		return [self.shortcut[c] for c in message]
		
	'''
	Decode from vector of int back to str
	'''
	def decode(self, buffer):
		return "".join([self.alphabetstr[i] for i in buffer])
		
	def ord(self, c):
		return self.shortcut[c]
		
	def chr(self, i):
		return self.alphabetstr[i]
		
	def len(self):
		return len(self.alphabetstr)
		
	def __len__(self):
		return self.len()
		
if __name__ == "__main__":
	a = Alphabet("abcdef")
	b = a.filter("abcdefghijklmno")
	print b
	assert(b == "abcdef")
	buffer = a.encode(b)
	print buffer
	assert(buffer == [0,1,2,3,4,5])
	m = a.decode(buffer)
	print m, b
	assert(m == b)
		
	
	

