"""
Practice with functions that do computations with values from paramters.
Some functions also return a value.
Docstrings MUST document parameters and return values.

lab3.py
Mihaela
9/19/17
"""

def check_fermat(a, b, c, n):
	"""
	Checks validity of Fermat's Last Theorem and prints out
	is Fermat was right or wrong.
	
	Fermat Last Theorem: there are no integers a,b,c, such that 
	a^n + b^n = c^n for any values of n greater 2.	

	a, b, c - integers
	n - integer greater than 2
	"""
	# check if n is greater than 2
	if n <= 2:
		print("n is less than or equal to 2")
	else: 
		print("{}^{} + {}^{} EQUAL TO {}^{} ???".format(a, n, b, n, c, n))

		# check if a^n + b^n = c^n
		first = pow(a, n) # set a equal to a^n
		second = pow(b, n) # set b equal to b^n
		result = pow(c, n) # set c equal to c^n
		print("{} + {} NOT EQUAL TO {} !!!".format(first, second, result))
		if first + second == result:
			print("Fermat was wrong!")
		else:
			print("Fermat was right!")

		
def is_triangle(a, b, c):
	"""
	Checks if the given values form a triangle and prints out yes or no.
	
	Triangle theorem: if any of the three lengths is greater
	than the sum of the other two, a triangle cannot be formed.

	Uses 2-branch conditional with OR for violating the theorem

	a, b, c - trhee positive numbers
	"""
	if (a > b + c) or (b > a + c) or (c > a + b):
		print("{}, {}, {} do NOT form a triangle".format(a, b, c))
	else:
		print("{}, {}, {} make a triangle".format(a, b, c))


def is_triangle2(a, b, c):
	"""
	Checks if the given values form a triangle and prints out yes or no.
	Uses 4-branch conditional for each possible violation of theorem
	   3 branches take into account 3 possible violations
	   last branch meets all 3 constraints

	a, b, c - three positive numbers
	"""	
	if (a > b + c):
		print("{} is bigger than {} + {}".format(a, b, c))
	elif (b > a + c):
		print("{} is bigger than {} + {}".format(b, a, c))
	elif (c > a + b):
		print("{} is bigger than {} + {}".format(c ,a, b))
	else:
		print("{}, {} and {} form a triangle".format(a ,b ,c))


