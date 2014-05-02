# Shift cipher:
# e(x) = (x + k) mod 26
# d(x) = (x - k) mod 26
#
# To work better with the alphabet, I assume ascii chars are used
# (256)

import random
from alphabet import Alphabet

def keygen(alphabet):
	return random.randint(1, len(alphabet))

def encrypt(key, message, alphabet):
	cipher = ""
	for c in message:
		cipher += alphabet.chr((alphabet.ord(c) + key) % len(alphabet))
	return cipher	

def decrypt(key, cipher, alphabet):
	message = ""
	for c in cipher:
		message += alphabet.chr((alphabet.ord(c) - key) % len(alphabet)) 
	return message
	

if __name__ == "__main__":
	a = Alphabet("ABCDEFGHIJKLMNOPQRSTUVXYZ ")
	k = keygen(a)
	print "Key:", k
	m = "ave caesar".upper()
	c = encrypt(k, m, a)
	print c
	assert(c != m)
	_m = decrypt(k, c, a)
	print _m
	assert(_m == m)
	
