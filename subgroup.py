#!/usr/bin/python

modulo = 11
for i in range(1, 11):
	subset = list()	
	power = 0
	member = (i ** power) % modulo
	while(member not in subset):
		subset.append(member)
		power += 1
		member = (i ** power) % modulo 	

	print "{0}: {1}: {2}".format(str(i), str(subset), str(len(subset))) 
	
					
