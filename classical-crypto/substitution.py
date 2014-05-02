import random
from alphabet import Alphabet

def keygen(alphabet):
	k = range(len(alphabet))
	random.shuffle(k)
	return k
	
def encrypt(key, message, alphabet):
	cipher = ""
	for c in message:
		cipher += alphabet.chr(key[alphabet.ord(c)])
	return cipher	

def decrypt(key, cipher, alphabet):
	message = ""
	for c in cipher:
		message += alphabet.chr(key.index(alphabet.ord(c)))
	return message
	
if __name__ == "__main__":
	alphabet = Alphabet("ABCDEFGHIJKLMNOPQRSTUVXYZ ")
	k = keygen(alphabet)
	print "Key:", k
	m = "substitution craziness"
	c = encrypt(k, m.upper(), alphabet)
	print "Ciphertext:",c
	assert(c != m)
	_m = decrypt(k, c, alphabet).lower()
	print "Message:",_m
	assert(_m == m)
