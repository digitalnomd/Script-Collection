#!/usr/bin/python
from math import log 

#This algorithm is an efficient way of 
#producing the modular exponentiation of a number.
#For example, to compute pow(a, b) mod n,
#this algorithm has a runtime of O(beta) instead of
#O(b) where b is the power and beta is the smallest
#number of bits that can be used to represent b.
#In practicality beta = lg(b).
#This algorithm is a variant the modular exponentiation algorithm 
#found in the Introduction to Algorithms textbook by CLRS.

def rev_mod_exp(a, b, n):
	d = 1
	k = int(log(b, 2)) 
	for i in range(0, k + 1):
		d = (d * d) % n
		if((i != k) and ((b & 1) == 1 or i == 0)):
			d = (d * a) % n
		b = b >> 1
	return d

if __name__ == "__main__":
	#test
	d = rev_mod_exp(7, 560, 561)
	print d
		
			
