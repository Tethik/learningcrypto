import random

def keygen():
	invertible = [(x,y) for x in range(256) for y in range(256) if (x*y) % 256 == 1]
	inv = random.choice(invertible)
	return (inv[0], random.randint(1, 256), inv[1])

def encrypt(key, message):
	cipher = ""
	for c in message:
		cipher += chr((ord(c) * key[0] + key[1]) % 256)
	return cipher	

def decrypt(key, cipher):
	message = ""
	for c in cipher:
		message += chr((key[2] * (ord(c) - key[1])) % 256) 
	return message

if __name__ == "__main__":
	k = keygen()
	print "Key:", k
	m = "Affine stands for what?"
	c = encrypt(k, m)
	print c
	assert(c != m)
	_m = decrypt(k, c)
	print _m
	assert(_m == m)
	
