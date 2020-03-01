def my_coroutine():
    while True:
        received = yield
        print("Received: ", received)


it = my_coroutine()
next(it)

it.send("First")
it.send("Second")


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


new_it = minimize()
next(new_it)
print(new_it.send(10))
print(new_it.send(4))
print(new_it.send(20))
print(new_it.send(-1))
