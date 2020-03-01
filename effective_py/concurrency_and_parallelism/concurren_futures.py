from time import time
from concurrent import futures


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [
    (1962323, 2262342),
    (2030677, 3814172),
    (1551645, 2229620),
    (2029045, 2020802)
]

start = time()
results = list(map(gcd, numbers))
print(results)
end = time()
print("TIME: %.3f" % (end - start))

new_start = time()
pool = futures.ProcessPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
new_end = time()
print("TIME: %.3f" % (new_end - new_start))
