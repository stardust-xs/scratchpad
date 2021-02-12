"""
Topics covered

accumulate
chain
combinations
combinations_with_replacement
compress
count:
    Creates an infinite counter.
    Takes two args at most, start and step.
cycle
dropwhile
filterfalse
groupby
islice
permutations
product
repeat
starmap
takewhile
tee
zip_longest:
    Zip multiple iterables together but considers only iterable with
    maximum length.
    Takes two args at most, *args and fillvalue.

"""
import itertools as i

# count()
# -------
# counter = i.count(2, 2)

# for d in counter:
#     if d > 20:
#         break
#     print(d) -> 2 4 6 8 10 12 14 16 18 20

# print(next(counter)) -> 2
# print(next(counter)) -> 4
# print(next(counter)) -> 6
# print(next(counter)) -> 8
# print(next(counter)) -> 10
# print(next(counter)) -> 12
# print(next(counter)) -> 14
# print(next(counter)) -> 16
# print(next(counter)) -> 18
# print(next(counter)) -> 20

# counter = i.count(2, -2)

# for d in counter:
#     if d < -20:
#         break
#     print(d, end=" ") -> 2 0 -2 -4 -6 -8 -10 -12 -14 -16 -18 -20

# zip_longest()
# -------------
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = ["a", "b", "c", "d", "e"]

# print([*zip(x, a)]) -> [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
# print([*i.zip_longest(x, a)]) -> [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, None), (6, None), (7, None), (8, None), (9, None)]
# print([*i.zip_longest(x, a, fillvalue="XA")]) -> [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'XA'), (6, 'XA'), (7, 'XA'), (8, 'XA'), (9, 'XA')]
