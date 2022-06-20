''' Контроль присваивания и извлечения атрибутов '''


class Human:
    '''
        Первый способ - через перехват всех атрибутов - методы __getattribute__ и __setattr__
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        print('Getting attribute', item)
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'age' and not isinstance(value, int):
            raise TypeError('Age must be Integer')
        else:
            # self.__dict__[key] = value # обращается к методку __getattribute__
            return object.__setattr__(self, key, value)  # не обращается к __getattribute__

class Human2:
    '''
        Второй способ - через функцию(декоратор) property()
    '''

    def __init__(self, name, age):
        self._name = name
        self._age = age
    def GetName(self):
        print('Property Get Name Trace')
        return self._name
    def GetAge(self):
        print('Property Get Age Trace')
        return self._age
    def SetAge(self, newage):
        print('Property Set Age Trace')
        self._age = newage
    name = property(GetName, None, None, None)
    age = property(GetAge, SetAge, None, None)

Andrey = Human2('Andrey', 33)
print(Andrey.name)
print(Andrey.age)
Andrey.age = 43
print(Andrey.age)
