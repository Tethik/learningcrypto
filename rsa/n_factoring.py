#!/usr/bin/python

import sys
import random

# From wikipedia: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def extended_gcd(a, b):		
	s, old_s = 0, 1
	r, old_r = b, a    
	while r != 0:
		quotient = old_r / r
		old_r, r = r, old_r - (quotient * r)
		old_s, s = s, old_s - (quotient * s)	
	return (old_r, s)

# Recover p and q from N with known e and d values.
# N = pq
# Source: http://www.ams.org/notices/199902/boneh.pdf
def factorN(N,e,d):
	k = d*e - 1
	t = 1
	r = k / 2
	while not r & 1:	
		t += 1
		r = r >> 1
	# k = 2^t*r
		
	while True:	
		g = random.randint(1, N)
		gc = extended_gcd(g, N)
		result = (int(abs(gc[0])), int(abs(gc[1])))	
		# If not 1, then g is actually sharing a factor (i.e. not coprime) with N. Since N only has two factors, gcd is a factor :)
		if not 1 in result: 
			return result			
					
		# g is coprime. Now we have 1/2 probability of finding a root of unity by squaring. 		
		part = pow(g, r, N)		
		for _ in xrange(t):		
			gc = extended_gcd(part - 1, N)			
			result = (int(abs(gc[0])), int(abs(gc[1])))	
			if 1 not in result:						
				return result	
			part *= part	
			
			
				
	
if __name__ == '__main__':	
	line = sys.stdin.readline().strip()
	while line != "":
		N, e, d = [int(v) for v in line.split(" ")]
		
		res = factorN(N,e,d)
		
		if res[0] < res[1]: # smallest factor first
			print res[0], res[1]
		else:
			print res[1], res[0] 
		line = sys.stdin.readline().strip()

