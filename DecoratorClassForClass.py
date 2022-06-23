def Decorator(cls):
    class InnerClass:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)
        def __getattr__(self, item):
            return self.instance.item
        def __repr__(self):
            return f'Name is {self.instance.name}, birthday {self.instance.birthday}'
    return InnerClass


class Decorator_class:

    class InnerClass:
        def __init__(self, cls, *args, **kwargs):
            print(cls, *args, **kwargs)
            self.instance = cls(*args, **kwargs)

        def __getattr__(self, item):
            return self.instance.item

        def __repr__(self):
            return f'Name is {self.instance.name}, birthday {self.instance.birthday}'

    def __init__(self, cls):
        self.cls = cls
    def __call__(self, *args, **kwargs):
        print(self.cls, *args, **kwargs)
        self.instance = Decorator_class.InnerClass(self.cls, *args, **kwargs)
        return self.instance

@Decorator_class
class Human:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

Andrey = Human('Andrey', '30.01.1989')
Andrey.name = 'Andrei'
print(Andrey.name)
print(Andrey)