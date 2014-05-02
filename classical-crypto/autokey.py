import random

def keygen():
	return random.randint(0, 256)
	
def encrypt(key, message):
	cipher = ""
	prev = key
	for c in message:
		cipher += chr((ord(c) + prev) % 256)
		prev = ord(c)
	return cipher
	
def decrypt(key, cipher):
	message = ""
	prev = key
	for c in cipher:
		m = (ord(c) - prev) % 256
		message += chr(m)
		prev = m
	return message


if __name__ == "__main__":	
	k = keygen()	
	m = "This is nearly just as bad as the shift cipher."		
	print "Key:", k
	c = encrypt(k, m)
	print c
	assert(c != m)
	_m = decrypt(k, c)
	print _m
	assert(_m == m)
