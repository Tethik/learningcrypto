# Keygen
# Generates RSA keys p and q.
# NOTE: This uses a deterministic random function. 
# Please don't use this for anything serious.
# Pretty please?

import random
import string
import math
import time


def getRandomPrime():	 
	n = random.randint(2,10000)
	while not isPrime(n):
		n = random.randint(2,10000)
	return n;

# Miller-Rabin primality test
# http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def isPrime(number):	
	
	# 2 is a prime (special case)
	if number == 2:
		return True
	
	# Handle 1,0,-1,...,-n cases.
	if number < 2:
		return False
	
	# If the number is even and not 2 it is not a prime.
	if (number & 1) < 1: 
		return False	
	
	# write n-1 as 2s·d by factoring powers of 2 from n-1	
	s = 0
	d = number-1
	while (math.ceil(d) & 1) < 1:
		s += 1
		d /= 2
	
	alist = {2,3,5,7,11,13,17}
	for a in alist:
		# Fermats theorem, if a^d = 1 mod number then number is coprime!		
		if pow(a,math.ceil(d),number) != 1:		
			truedat = True			
			for r in range(s):
				truedat &= (pow(a, 2**r * math.ceil(d), number) != number-1)								
			if(truedat):				
				return False			
	return True
	
def isCoprime(number1, number2):
	return number1 % number2 > 0

random.seed(time.time())

p = getRandomPrime()
q = getRandomPrime()
print ("p: {0}, q: {1}".format(p,q))

n = p*q;
print("n: {0}".format(n))

eut = (p-1)*(q-1)
print("eut: {0}".format(eut))

e = 2
for i in range(math.floor(eut/3),eut):
	if(isCoprime(n,i)):
		e = i
		break
print("e: {0}".format(e))

d = 1;
for i in range(1,eut):
	if(i*e % eut == 1):
		d = i
		break
print("d: {0}".format(d))





