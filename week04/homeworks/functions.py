# -*- coding: utf-8 -*-

def square(num):
	"""
	Задание 1. Напишите функцию, которая возвращает
	квадрат числа num
	
	>>> square(1)
	1
	>>> square(2)
	4
	>>> square(0)
	0
	>>> square(-1)
	1
	>>> square(5)
	25
	"""
	return num * num

def cube(num):
	"""
	Задание 2. Напишите функцию, которая возвращает
	куб числа num
	
	>>> cube(1)
	1
	>>> cube(2)
	8
	>>> cube(0)
	0
	>>> cube(-1)
	-1
	>>> cube(5)
	125
	"""
	pass

def listOfSquare(lst):
	"""
	Задание 3. Напишите функцию, которая принимает
	список чисел и возвращает список квадратов этих чисел
	
	>>> listOfSquare([1])
	[1]
	>>> listOfSquare([1, 2])
	[1, 4]
	>>> listOfSquare([0, 5, 3])
	[0, 25, 3]
	>>> listOfSquare([-1, 1, 2])
	[1, 1, 4]
	>>> listOfSquare([5, 6, 7])
	[25, 36, 49]
	"""
	pass

def filterEvenNumbers(lst):
	"""
	Задание 4. Напишите функцию, которая принимает
	список чисел и возвращает список из четных чисел
	
	>>> filterEvenNumbers([1])
	[]
	>>> filterEvenNumbers([1, 2])
	[2]
	>>> filterEvenNumbers([0, 5, 3])
	[0]
	>>> filterEvenNumbers([-1, 1, 2])
	[2]
	>>> filterEvenNumbers([5, 6, 7, 8, 10])
	[6, 8, 10]
	"""
	pass

def fizzbuzz(num):
	"""
	Напишите программу для печати Fizz, Buzz или FizzBuzz, если выполняется одно из условий.
	Если число кратно 3, печать Fizz; если кратно 5, печать Buzz;
	и если одновременно кратно 3 и 5 - печать FizzBuzz.
	
	>>> fizzbuzz(6)
	Fizz
	>>> fizzbuzz(10)
	Buzz
	>>> fizzbuzz(15)
	FizzBuzz
	>>> fizzbuzz()
	None
	"""
	pass
	
def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
