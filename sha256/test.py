#!/usr/bin/python

import random
import string
import unittest
import sha256
from Crypto.Hash import SHA256 # to test against.

class TestCrt(unittest.TestCase):
	def test_against_real_implementation(self):
		self.assertEquals(SHA256.new("").hexdigest(), sha256.hash(""))
		
		for _ in xrange(10000):
			length = random.randint(3,1024)
			random_string = "".join([random.choice(string.letters) for _ in xrange(length)])
			real_hash = SHA256.new(random_string).hexdigest()
			my_hash = sha256.hash(random_string)
			self.assertEquals(len(real_hash), len(my_hash))
			self.assertEquals(real_hash, my_hash)
			
	def test_preprocessing(self):
		value = "abc"
		self.assertEquals([0x61, 0x62, 0x63, 0x80], sha256.padding(value)[0:4])
		
	def test_byte_array_conversion(self):
		v = [ 0x68, 0x65, 0x6A ]		
		self.assertEquals(v, sha256.convert_to_bytes_array_mod512("hej"))
	
	def test_convert_int64_to_byte(self):
		x = 1245427
		v = [0]*5 + [0x13, 0x00, 0xf3]
		
		self.assertEquals(v, sha256.convert_int64_to_bytes(x))
		
	def test_rightrotate(self):
		x = 1
		self.assertEquals(1 << 31, sha256.rotr(x, 1))
		self.assertEquals(1 << 31, sha256.rotr(2, 2))
		self.assertEquals((1 << 31) + (1 << 30), sha256.rotr(3, 2))
		self.assertEquals((1 << 31) + 1, sha256.rotr(3, 1))
		self.assertEquals(132, sha256.rotr(132, 0))
	
		
if __name__ == '__main__':
    unittest.main()
