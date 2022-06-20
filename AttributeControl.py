''' Контроль присваивания и извлечения атрибутов '''
import datetime
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
        Второй способ - через функцию(декоратор) property(). _age - вычисляемый атрибут
    '''

    def __init__(self, name, birthday):
        self._name = name
        self.birthday = birthday
    def GetName(self):
        print('Property Get Name Trace')
        return self._name

    def SetName(self, newname):
        print('Property Set Name Trace')
        self._name = newname

    def GetAge(self):
        print('Property Get Age Trace')
        return int(datetime.datetime.now().year) - int(self.birthday.split('.')[2])

    name = property(GetName, SetName, None)
    age = property(GetAge, None, None)

class Human3:
    '''
        Функционал с исползованием декораторов @property
    '''
    def __init__(self, name, birthday):
        self._name = name
        self.birthday = birthday
    @property
    def name(self):
        print('Property Get Name Trace')
        return self._name
    @name.setter #setter - это метод свойства
    def name(self, newname):
        print('Property Set Name Trace')
        self._name = newname
    @property
    def age(self):
        print('Property Get Age Trace')
        return int(datetime.datetime.now().year) - int(self.birthday.split('.')[2])

class DescAttributesAge:
    def __get__(self, instance, owner):
        return int(datetime.datetime.now().year) - int(instance.birthday.split('.')[2])
class Human4:
    '''
        Функционал с использованием дескрипторов
    '''
    age = DescAttributesAge() # Вычисляемый дескриптором атрибут
    def __init__(self, name, birthday):
        self._name = name
        self.birthday = birthday



Andrey = Human4('Andrey', '30.01.1989')
print(Andrey._name)
print(Andrey.age)
