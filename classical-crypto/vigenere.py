
def encrypt(key, message):
	cipher = ""
	i = 0
	for c in message:
		cipher += chr((ord(c) + ord(key[i])) % 256)
		i = (i+1) % len(key)
	return cipher
	
def decrypt(key, cipher):
	message = ""
	i = 0
	for c in cipher:
		message += chr((ord(c) - ord(key[i])) % 256)
		i = (i+1) % len(key)
	return message

if __name__ == "__main__":
	k = "16th century"
	print "Key:", k
	m = "Blaise de Vigenere"
	c = encrypt(k, m)
	print c
	assert(c != m)
	_m = decrypt(k, c)
	print _m
	assert(_m == m)
