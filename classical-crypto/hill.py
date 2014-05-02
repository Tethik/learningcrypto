import numpy
import math
from numpy import matrix
from numpy import linalg
from numpy import dot
import random

#
# Matrix inverse code copied from StackOverflow user John:
# http://stackoverflow.com/a/4293123
#
def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor
#
# End of Copy-pasta
#

def dotMod(A, B, p):
	C = dot(A,B)
	#~ print C
	for i in xrange(len(C)):
		C[i] = C[i] % p
	return C
	
def pad(key, message):
	block_size = len(key)
	# Silly way of padding
	for _ in range(len(message) % block_size):
		message += " "
	return message

def keygen(m):
	# We need a matrix of size m*m which is invertible.
	# Going to be lazy and just iterate until we find one via random
	# heuristic.
	while True:
		potential_key = []
		for _ in range(m):
			potential_key.append([random.randint(1,256) for _ in range(m)])			
		try:
			modMatInv(potential_key, 256)
			return potential_key
		except:
			pass	

def encrypt(key, message):		
	#~ print "Encrypting.."
	block_size = len(key)
	cipher = ""
	i = 0
	while i < len(message):
		block = [ ord(c) for c in message[i:i+block_size] ]
		#~ print block
		encrypted_block = dotMod(block, key, 256)
		for ec in encrypted_block:
			cipher += chr(ec)
		i += block_size
		
	return cipher
	
def decrypt(key, cipher):
	#~ print "Decrypting.."
	block_size = len(key)
	kinv = modMatInv(key, 256)
	message = ""
	i = 0
	while i < len(cipher):
		block = [ ord(c) for c in cipher[i:i+block_size] ]
		decrypted_block = dotMod(block, kinv, 256)
		#~ print decrypted_block
		for ec in decrypted_block:
			message += chr(int(ec))
		i += block_size
	
	return message

if __name__ == "__main__":
	k = keygen(2)
	print "Key:", k
	m = pad(k, "Meet me under the tunnel. ")
	c = encrypt(k, m)
	print c
	assert(c != m)
	_m = decrypt(k, c)
	print _m
	assert(_m == m)
