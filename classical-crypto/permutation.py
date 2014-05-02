import random

def pad(key, message):
	block_size = len(key)
	# Silly way of padding
	for _ in range(len(message) % block_size):
		message += " "
	return message

def keygen(m):
	key = range(m)
	random.shuffle(key)
	return key
	
def encrypt(key, message):
	block_size = len(key)	
	cipher = ""
	i = 0
	while i < len(message):
		block = message[i:i+block_size]
		encrypted_block = [ block[key[c]] for c in xrange(len(block)) ]
		cipher += "".join(encrypted_block)
		i += block_size		
	return cipher
	
def decrypt(key, cipher):
	block_size = len(key)	
	message = ""
	i = 0
	while i < len(cipher):
		block = cipher[i:i+block_size]
		paired_block = [ (block[c], key[c]) for c in xrange(block_size) ]		
		encrypted_block = [ b[0] for b in sorted(paired_block, key=lambda b: b[1]) ]	
		message += "".join(encrypted_block)			
		i += block_size		
	return message

if __name__ == "__main__":	
	print "# Test with keysize = len(m)"
	m = "We're just switching which letters go where. "
	k = keygen(len(m))
	m = pad(k, m)
	print "Key:", k
	c = encrypt(k, m)
	print c
	assert(c != m)
	_m = decrypt(k, c)
	print _m
	assert(_m == m)
	
	print
	print "# Test with keysize < len(m)"
	k = keygen(10)
	print "Key:", k
	m = pad(k, m)	
	c = encrypt(k, m)
	print c
	assert(c != m)
	_m = decrypt(k, c)
	print _m
	assert(_m == m)
	
