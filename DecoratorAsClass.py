
class Decorator:
    '''
        Декоратор в виде класса (не будет работать с методами другого класса, ниже пояснено почему)
    '''
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print(self, *args, **kwargs)
        return 'Start Decorator\n' + str(self.func(*args, **kwargs)) + '\nStop Decorator'

#@Decorator
#def mult(a, b):
#    return a * b
#print(mult(2, 2)) # Все работает нормлально

class Test:
    '''
        При декорировании метода в экземпляр попадает не обьект класса, а обьект
        декоратора - в данном случае в селфе будет обьект printa
    '''
    a = 1
    @Decorator
    def printa(self):
        print(Test.printa)
        return self.a

a = Test()
#print(a.printa()) - ошибочный вызов, даст ошибку
print(Test.printa(a)) # а вот так все сработает

