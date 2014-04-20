#!/usr/bin/python

from Crypto.Hash import SHA256
from optparse import OptionParser
options = OptionParser(usage='%prog', description='Calculate sha256 hash')
import copy, sys

#~ h0 = 0x6a09e667
#~ h1 = 0xbb67ae85
#~ h2 = 0x3c6ef372
#~ h3 = 0xa54ff53a
#~ h4 = 0x510e527f
#~ h5 = 0x9b05688c
#~ h6 = 0x1f83d9ab
#~ h7 = 0x5be0cd19



k = [
   0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
   0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
   0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
   0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
   0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
   0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
   0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
   0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2 ]
   
# 512 bits = 64 bytes
def convert_to_bytes_array_mod512(value):
	return [b for b in bytearray(value)]	
		
def convert_int64_to_bytes(i):
	return [(i >> shift) & 0xFF for shift in range(56, -8, -8)]
	
def appendbit(bytes, bit):
	assert(abs(bit) < 2)
	prev = bit
	for i in xrange(len(bytes) - 1, -1, -1):
		bytes[i], prev = (bytes[i] << 1 | prev) & 0xFF, bytes[i] >> 7
	return bytes
	
def padding(value):
	bytes = convert_to_bytes_array_mod512(value)
	orig_length = len(value)
	#~ bytes = appendbit(bytes, 1)
	bytes += [0x80]
		
	bits = 0
	while len(bytes) % 64 != 56:
		bytes += [0]
		#~ if bits % 8 == 0:
			#~ bytes = [0] + bytes
		#~ bytes = appendbit(bytes, 0)
		#~ bits += 1
	return bytes

def preprocess(value):
	orig_length = len(bytearray(value)) * 8
	bytes = padding(value)		
	
	# move 64 / 8 = 8 bytes to the left.
	bytes = bytes + convert_int64_to_bytes(orig_length)
	#~ print len(bytes)
	assert(len(bytes) % 64 == 0)
	return bytes

def hash(value):
	# initial values
	h = [ 0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19 ]	
	
	modulo = 2 ** 32
	# make into 64 byte chunks
	chunks = preprocess(value)
	# iterate through each
	for c in xrange(0, len(chunks) / 64, 64):
		chunk = chunks[c:(c+64)]
		
		print "Block contents:"
		for i in xrange(0, len(chunk), 4):
			print "W["+str(i/4)+"] = ", [hex(v) for v in chunk[i:i+4]]
		print 
		
		w = chunk[0:16] + [0]*48 # message schedule array
		
		for i in xrange(16, 63):
			s0 = (w[i - 15] >> 7) ^ (w[i - 15] >> 18) ^ (w[i - 15] >> 3)
			s1 = (w[i - 2] >> 17) ^ (w[i - 2] >> 19) ^ (w[i - 2] >> 10)
			w[i] = (w[i - 16] + s0 + w[i - 7] + s1) % modulo

		wh = copy.deepcopy(h) #working values
		
		# compression function mainloop
		for i in xrange(0, 64):
			s1 = (wh[4] >> 6) ^ (wh[4] >> 11) ^ (wh[4] >> 25)
			ch = (wh[4] & wh[5]) ^ ((~wh[4]) & wh[6])
			temp1 = (wh[7] + s1 + ch + k[i] + w[i]) % modulo
			s0 = (wh[0] >> 2) ^ (wh[0] >> 13) ^ (wh[0] >> 22)
			maj = (wh[0] & wh[1]) ^ (wh[0] & wh[2]) ^ (wh[1] & wh[2])
			temp2 = (s0 + maj) % modulo
			
			for s in xrange(7, 0, -1):
				wh[s] = wh[s-1]
			wh[4] = (wh[4] + temp1) % modulo
			wh[0] = (temp1 + temp2) % modulo
			print "t = "+str(i)+" ", [hex(c) for c in wh]
		
		i = 0
		while i < len(h):
			h[i] = (h[i] + wh[i]) % modulo
			i += 1
			
	hxdigest = "".join([hex(v).replace("0x", "").replace("L","") for v in h])
	return hxdigest

if __name__ == "__main__":
	opts, args = options.parse_args()
	if len(args) > 0:
		print hash(args[0])
		exit(0)
		
	line = sys.stdin.readline().strip()
	while line != "":
		print hash(line)
		line = sys.stdin.readline().strip()
