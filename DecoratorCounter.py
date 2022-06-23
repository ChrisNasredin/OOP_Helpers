def counter(func):
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        print('number of call func %s - %s' % (func, counter))
        counter += 1
        return func(*args, **kwargs)
    return inner
@counter
def exp(num, exp):
    return (num ** exp)

print(exp(4,5))
print(exp(4,5))
print(exp(4,5))
