#!/usr/bin/python
import unittest
import n_factoring

class TestFactoring(unittest.TestCase):
	def runTest(self):
		cases = [((299,5,53),(13,23)),
				 ((85,3,43), (5,17)),
				 ((22,3,7), (2,11)),
				 ((899,11,611), (29,31)),
				 ((55,3,27), (5,11))]		
		for _ in range(1000): # some testing here so that we hopefully dont end up in a never ending loop...
			for case in cases:
				res = n_factoring.factorN(*case[0])	
				self.assertItemsEqual(case[1], res)			

if __name__ == '__main__':
    unittest.main()
