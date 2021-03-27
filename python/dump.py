import itertools

# count
# cycle
# repeat
# starmap

# cnt = itertools.count()

# def count(start=0, step=1):
#     start = start
#     while True:
#         yield start
#         start += step

# repeat = itertools.repeat('xa', 5)

# def rpt(obj, times):
#     while times > 0 :
#         yield obj
#         times -= 1

# cyc = itertools.cycle([1, 2, 3, 4, 5])

# def cycle(ite):
#     while True:
#         for i in ite:
#             yield i

import functools

def cachec(func):
    cached_data = {}

    @functools.wraps(func)
    def dec(*args, **kwargs):
        try:
            print('before', cached_data)
            return (cached_data[args])
        except KeyError:
            cached_data[args] = ret = func(*args, **kwargs)
            print('after', cached_data)
            return ret

    return dec


@cachec
def compute(n):
    print('this is with', n)
    return n ** 2
