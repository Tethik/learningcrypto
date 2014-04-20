#!/usr/bin/python

import unittest
import sha256
from Crypto.Hash import SHA256 # to test against.

class TestCrt(unittest.TestCase):
	def test_against_real_implementation(self):
		for _ in xrange(10000):
			random_string = "".join(random.sample(string.letters, 10))
			self.assertEquals(SHA256.new(random_string).digest(), sha256.hash(random_string))
			
	def test_something_else(self):
		pass
		
if __name__ == '__main__':
    unittest.main()
