'''
Пример декорирования метода класса декоратором класса
'''

def decorator_as_func(func):
    def inner(*args, **kwargs):
        print(*args, **kwargs)
        return func(*args, **kwargs)

    return inner


class decorator_as_class:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(self, *args, **kwargs)
        self.func(*args, **kwargs)


class Human:
    def __init__(self, name):
        self.name = name

    @decorator_as_func
    def setage(self, age):
        self.age = age

    @decorator_as_class
    def setjob(self, job):
        '''
        Не сработает из за аргумента self. В self в декораторе окажется экзамепляр декоратора, а не экземпляр human
        Экземпляр  Human в этом случае просто не передается.
        '''
        self.job = job


Andrey = Human('Andrey')
Andrey.setage(33)
print(Andrey.age)
Andrey.setjob('Developer')
print(Andrey.job)
