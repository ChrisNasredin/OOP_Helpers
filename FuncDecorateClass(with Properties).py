def decoHuman(cls):
    class Inner:
        def __init__(self, *args, **kwargs):
            self.HumanInst = cls(*args, **kwargs)
        @property
        def name(self):
            print('getter work')
            return self.HumanInst.name
        @name.setter
        def name(self, new_name):
            print('setter work')
            self.HumanInst.name = new_name
        def __getattr__(self, item):
            return getattr(self.HumanInst, item)
    return Inner


@decoHuman
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Andrey = Human('Andrey', 33)
print(Andrey.name)
Andrey.name = 'Andrei'
print(Andrey.name)