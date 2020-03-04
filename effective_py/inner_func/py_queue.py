from heapq import heappush, heappop

a = []
heappush(a, 5)
heappush(a, 4)
heappush(a, 3)
heappush(a, 7)

print(heappop(a), heappop(a), heappop(a))
