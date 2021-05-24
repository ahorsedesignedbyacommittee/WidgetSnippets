littlemathematics is a simple module that includes functions douing some small mathematical stuff. 
The practical usefulness is limited, as there are certainly modules out there that achieve the same reuslts more efficiently.
Nonetheless, it may be amusing to see what is going on inside the black box.

So far, littlemathematics includes two functions:
littlemathematics.eratosthenes()
littlemathematics.pimaker()

--------------------------------------------------------------------------------------------

littlemathematics.eratosthenes()


The syntax of this function is:
littlemathematics.eratosthenes(limit)

whereby limit is an integer representing the number up to which (and including) prime numbers are to be searched.
The function uses the ancient "sieve of Eratosthenes" to find prime numbers: 
It starts with a raw list up to (and including) the given limit and then removes, subsequently, all numbers that are multiples of smaller integers.
The resulting list (which constitutes the output of the function) includes all primes up to and including the given limit.

--------------------------------------------------------------------------------------------

littlemathematics.pimaker()


The syntax of this function is:
littlemathematics.pimaker(i)

where i is the number of iterations of the algorithm you wish to perform.

The function uses the Bailey-Borwein-Plouffe (BPP) formula to iteratively compute approximations of pi. The output is a tuple with two floating point numbers; the first is the approximation of pi as calculated by the algorithm, the second is the absolute of the difference between that approximation and the value of pi as stored in the math module of Python. You will see that this difference becomes very small even after few iterations.

--------------------------------------------------------------------------------------------
Version 2.1, May 2021
