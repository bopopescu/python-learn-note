import bisect
import time

x = list(range(10 ** 6))
print(time.time())
i = x.index(99332)
print(i)
print(time.time())

new_i = bisect.bisect_left(x, 5023)
print(new_i)
