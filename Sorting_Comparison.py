# Sorting Comparison (Сравнение сортировок)

from random import randint
from functools import partial
import timeit

def generating_random_array (N):
	''' Генерирует массив случайных чисел, в котором число элементов равно переданному числу N '''
	random_array = []
	for x in range (N):
		r_num = randint (0, N)
		random_array.append (r_num)
	return random_array
	
def insert_sort (A):
	''' Сортировка массива методом вставками (insert sort) '''
	N = len (A)
	for x in range (1, N):
		k = x
		while k > 0 and A[k-1] > A[k]:
			A[k], A[k-1] = A[k-1], A[k]
			k -= 1

def choise_sort (A):
	''' Сортировка массива методом выбора (choise sort)'''
	N = len (A)
	for i in range (0, N-1):
		for j in range (i+1, N):
			if A[j] < A[i]:
				A[j], A[i] = A[i], A[j]
				
def bubble_sort (A):
	''' Сортировка массива методом пузырька (bubble sort) '''
	N = len (A)
	for x in range (1, N):
		for k in range (0, N-x):
			if A[k] > A[k+1]:
				A[k], A[k+1] = A[k+1], A[k]
				
def sorted_python (A):
	''' Функция сортировки Python - sorted ()'''
	sorted (A)

def runtime_function (function, array):
	''' Возвращает время выполнения сортировки переданной функцией и переданного массива '''
	times = min (timeit.Timer(partial(function, array)).repeat(7, 1000))
	return times

list_func = [insert_sort, choise_sort, bubble_sort, sorted_python]
a = generating_random_array (100) # можно сделать по запросу от пользователя
for x in list_func:
	print (x.__doc__)
	t = runtime_function (x, a[:])
	print (f'Массив отсортирован за {t} сек')

