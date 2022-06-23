def decorator(a,b):
    print(a,b, 'args')
    def realdecortator(func):
        def inner(*args, **kwargs):
            return 'start\n' + str(func(*args, **kwargs)) + '\nstop'
        return inner
    return realdecortator
@decorator(1,2)
def plus(x, y):
    return x + y

print(plus(2,2))