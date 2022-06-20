def counter(func):
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        print(counter, 'number of call')
        counter += 1
        return func(*args, **kwargs)
    return inner

def sq(a):
    print(a ** 2)
sq = counter(sq)

sq(2)
sq(5)

