littlemathematics is a simple module that includes functions douing some small mathematical stuff. 
The practical usefulness is limited, as there are certainly modules out there that achieve the same reuslts more efficiently.
Nonetheless, it may be amusing to see what is going on inside the black box.

So far, littlemathematics includes one function:
littlemathematics.eratosthenes()

--------------------------------------------------------------------------------------------

littlemathematics.eratosthenes()


The syntax of this function is:
littlemathematics.eratosthenes(limit)

whereby limit is an integer representing the number up to which (and including) prime numbers are to be searched.
The function uses the ancient "sieve of Eratosthenes" to find prime numbers: 
It starts with a raw list up to (and including) the given limit and then removes, subsequently, all numbers that are multiples of smaller integers.
The resulting list (which constitutes the output of the function) includes all primes up to and including the given limit.

--------------------------------------------------------------------------------------------
Version 1.0, May 2021
