from typing import List

x = [9, 15, 12, 74, 56, 32, 45, 10, 5]


def sort(x: List) -> List:
	'''Sort using Bubble sort algorithm.'''

	passes = len(x) - 1
	for j in range(passes):
		for i in range(passes - j):
			if x[i + 1]:
				print(f'{x} -> Comparing {x[i]} & {x[i + 1]}')
				if x[i] > x[i + 1]:
					curr, next = x[i], x[i + 1]
					x[i], x[i + 1] = next, curr
		print(f'Pass #{j + 1} completed')
	return x


print(sort(x))
