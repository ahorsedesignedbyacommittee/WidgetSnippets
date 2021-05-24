------------------------------------------------------------------------------------------------------------

def eratosthenes (limit):

	raw_list = [number for number in range(2, limit+1)]
	for x in raw_list:
		multiples_x = [x * multiple for multiple in range(2, limit) if x * multiple <= limit]
		for multiple in multiples_x:
			try:
				raw_list.remove(multiple)
			except:
				pass
	return raw_list

------------------------------------------------------------------------------------------------------------

def pimaker(p):
	
	k = 0
	v = 0
	while k < p:
		f1 = 1/16**k
		f2 = (4/(8*k + 1)) - (2/(8*k + 4)) - (1/(8*k + 5)) - (1/(8*k + 6))
		v += f1 * f2
		k += 1
	from math import pi
	return (v, abs(pi-v))

------------------------------------------------------------------------------------------------------------

def montecarlopi(p):
	
	from random import randrange
	from math import sqrt, pi
	hits = 0
	for n in range(1, p+1):
		x = randrange(0, 100000)
		y = randrange(0, 100000)
		if sqrt (x**2 + y ** 2) <= 100000:
			hits += 1
	v = (hits/p) * 4
	return (v, abs(pi-v))
