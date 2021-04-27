from typing import Union

x = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]


def binary_search(x: list, a: int) -> Union[int, str]:
	x.sort()
	print(x)
	l, r = 0, len(x) - 1
	while l < r:
		mid = (l + r) // 2
		print(l, r, mid)
		if x[mid] == a:
			return mid
		elif x[mid] > a:
			r = mid - 1
		elif x[mid] < a:
			l = mid  + 1
	else:
		return 'Not present in the list!'


print(binary_search(x, 42))
