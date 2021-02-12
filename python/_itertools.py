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
zip_longest

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
