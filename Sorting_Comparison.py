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
				
def sort_python (A):
	''' Сортировка массива методом sort ()'''
	A.sort ()
	
def sorted_python (A):
	''' Функция сортировки Python - sorted () '''
	sorted (A)
	
def hoar_sort (A):
	''' Сортировка массива методом Тони Хоара '''
	if len (A) <= 1:
		return
	L = []
	M = []
	R = []
	n = A[0]
	for x in A:
		if x < n:
			L.append (x)
		elif x == n:
			M.append (x)
		else:
			R.append (x)
	hoar_sort (L)
	hoar_sort (R)
	k = 0
	for x in L + M + R:
		A[k] = x
		k += 1
		
def merge (A:list, B:list):
	''' Слияние отсортированных масивов '''
	C = [0] * (len(A) + len(B))
	i = k = n = 0
	while i < len(A) and k < len(B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return C
	
def merge_sort (A):
	''' Сортировка массива слиянием '''
	if len(A) <= 1:
		return
	middle = len(A)//2
	L = [A[i] for i in range (0, middle)]
	R = [A[i] for i in range (middle, len(A))]
	merge_sort (L)
	merge_sort (R)
	C = merge (L, R)
	for i in range (len(A)):
		A[i] = C[i]

def runtime_function (function, array):
	''' Возвращает время выполнения сортировки переданной функцией и переданного массива '''
	times = min (timeit.Timer(partial(function, array)).repeat(7, 1000))
	return times

list_func = [insert_sort, choise_sort, bubble_sort, sort_python, sorted_python, hoar_sort, merge_sort]
a = generating_random_array (100) # можно сделать по запросу от пользователя
for x in list_func:
	print (x.__doc__)
	t = runtime_function (x, a[:])
	print (f'Массив отсортирован за {t} сек\n')

