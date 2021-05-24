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
