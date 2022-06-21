import datetime


class Descriptor:
    def __set_name__(self, owner, name):
        '''
            При обращении к обьекту класса (а по совместительству атрибуту класса Human
            мы получаем имя атрибута и присоединяем его в качестве атрибута к обьекту атрибута
            (СЛОЖНА) - это сделано для того, чтобы имя name было доступно в других методах по
            ссылке self.var_name
            другими словами, после того, как мы обращаемся к атрибуту, педе get или set мы
            получаем имя, которое нужно обработать в self.var_name
        '''
        self.var_name = '_' + name

    def __get__(self, instance, owner):
        print('Descriptor Get Working')
        if self.var_name == '_age':
            return int(datetime.datetime.now().year) - int(instance._birthday.split('.')[2])
        return getattr(instance, self.var_name)
    def __set__(self, instance, value):
        print('Descriptor Set Working')
        if self.var_name == '_age':
            print('Age is dynamic Attribute. You can\'t install age manual')
        if self.var_name == '_name':
            if not isinstance(value, str):
                print('Только строка')
            else:
                setattr(instance, self.var_name, value)

class Human:
    age = Descriptor()  # вычисляемый атрибут
    name = Descriptor()
    birthday = Descriptor()

    def __init__(self, name, birthday):
        self._name = name
        self._birthday = birthday


Andrey = Human('Andrey', '30.01.1989')
Andrey.age = 123
print(Andrey.age)
print(Andrey.name)