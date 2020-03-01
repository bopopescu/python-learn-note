from collections import namedtuple

Query = namedtuple("Query", ("y", "x"))
ALIVE = "*"
EMPTY = "-"


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 1)
    ne = yield Query(y + 1, x + 1)
    e_ = yield Query(y + 1, x + 1)
    se = yield Query(y + 1, x + 1)
    s_ = yield Query(y + 1, x + 1)
    sw = yield Query(y + 1, x + 1)
    w_ = yield Query(y + 1, x + 1)
    nw = yield Query(y + 1, x + 1)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


it = count_neighbors(10, 5)
q1 = next(it)

print("First yield:", q1)
q2 = it.send(ALIVE)
print("Second yield:", q2)
