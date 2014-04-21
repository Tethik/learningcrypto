#!/usr/bin/python

from optparse import OptionParser
options = OptionParser(usage='%prog', description='Calculate sha256 hash')
import copy, sys

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
	bytes += [0x80]
		
	bits = 0
	while len(bytes) % 64 != 56:
		bytes += [0]
	return bytes

def preprocess(value):
	orig_length = len(bytearray(value)) * 8
	bytes = padding(value)		
	
	# move 64 / 8 = 8 bytes to the left.
	bytes = bytes + convert_int64_to_bytes(orig_length)
	assert(len(bytes) % 64 == 0)
	return bytes
	
def rotr(value, offset):
	return (value >> offset) | (value << (32 - offset)) % (1 << 32)

def sigma0(value):
	return rotr(value, 7) ^ rotr(value, 18) ^ (value >> 3)
	
def sigma1(value):		
	return rotr(value, 17) ^ rotr(value, 19) ^ (value >> 10)
	
def ch(x,y,z):
	return (x & y) ^ ((~x) & z)
	
def maj(x,y,z):
	return (x & y) ^ (x & z) ^ (y & z)
	
def sum0(x):
	return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
	
def sum1(x):
	return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
	
def formathex(x):
	h = hex(x).replace("0x", "").replace("L","")
	return "0"*(8-len(h))+h

def hash(value):
	# initial values
	H = [ 0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19 ]	
	
	modulo = 1 << 32
	# make into 64 byte chunks
	chunks = preprocess(value)
	# iterate through each
	for c in xrange(0, len(chunks), 64):
		chunk = chunks[c:(c+64)]
		
		w = [0]*64
		
		for i in xrange(0, len(chunk), 4):
			w[i / 4] = (chunk[i] << 24) | (chunk[i+1] << 16) | (chunk[i+2] << 8) | (chunk[i+3])
		
		for i in xrange(16, 64):			
			w[i] = (w[i-16] + sigma0(w[i-15]) + w[i-7] + sigma1(w[i-2])) & 0xFFFFFFFF
			
		#~ print "W contents:"
		#~ for i in xrange(0, len(chunk), 4):
			#~ print "W["+str(i/4)+"] = ", [hex(v) for v in w[i:i+4]]
		#~ print 

		a = H[0]
		b = H[1]
		c = H[2]
		d = H[3]
		e = H[4]
		f = H[5]
		g = H[6]
		h = H[7]
		
		# compression function mainloop
		for i in xrange(64):
			temp1 = (h + sum1(e) + ch(e,f,g) + k[i] + w[i]) & 0xFFFFFFFF
			temp2 = (sum0(a) + maj(a,b,c)) & 0xFFFFFFFF
			
			h = g
			g = f
			f = e
			e = (d + temp1) & 0xFFFFFFFF
			d = c
			c = b
			b = a
			a = (temp1 + temp2) & 0xFFFFFFFF
		
		# ugly, but trying to get this to work.
		H[0] = (H[0] + a) & 0xFFFFFFFF
		H[1] = (H[1] + b) & 0xFFFFFFFF
		H[2] = (H[2] + c) & 0xFFFFFFFF
		H[3] = (H[3] + d) & 0xFFFFFFFF
		H[4] = (H[4] + e) & 0xFFFFFFFF
		H[5] = (H[5] + f) & 0xFFFFFFFF
		H[6] = (H[6] + g) & 0xFFFFFFFF
		H[7] = (H[7] + h) & 0xFFFFFFFF
		
			
	hxdigest = "".join([formathex(v) for v in H])
	return hxdigest

if __name__ == "__main__":
	opts, args = options.parse_args()
	if len(args) > 0:
		print hash(args[0])
		exit(0)
		
	line = sys.stdin.readline().strip()
	while line != "":
		print hash(line.decode('hex'))
		line = sys.stdin.readline().strip()
	print
	
