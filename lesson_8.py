# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
class Data_str:
    def __init__(self,dt):
        self.dt = dt

    def data_pr(self):
        a = []
        a = self.dt.split(".")
        for i in range(3):
            a[i] = int(a[i])
        self.pr(a)
        return a

    @classmethod
    def data_ch(cls, ndt):
        cls.dt = ndt

    @staticmethod
    def pr(a):
        if a[0] > 31 or a[0] < 1:
            print('число вне диапазона дат 1-31')
        if a[1] >12 or a[1] <1:
            print('месяц вне диапазаона 1-12')
        if a[2] < 1900:
            print('формат года не в формате 19хх или 20хх')
# #
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
#
class Div(Exception):
    def __init__(self, var):
        self.var = var

a = input('введите делимое: ')
b = input('введите делитель: ')
try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise Div('Деление на ноль')
except ValueError:
    print('введите числа')
except Div as err:
    print(err)
else:
    print(a/b)
#



# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
#
class Only_num(Exception):
    def __init__(self, var):
        self.var = var

sp_var = []
i = 0
while True:
    if input('для остановки ввода введите stop для продолжение enter: ') == 'stop':
        break
    i += 1
    var_add = True
    try:
        var_0 = input(f'введите {i}-е число: ')
        for var in var_0:
            if var in '0123456789':
                pass
            else:
                raise Only_num('Введите число')
                break
    except Only_num as err:
        print(err)
        i -= 1
        var_add = False
    if var_add:
        sp_var.append(int(var_0))
print(sp_var)





# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
#
#



class Orgteh: # на сколько успел, долго не складывалось что хотелось отразить :) по факту реализовал учет и перемещение между складами
    sklad = {}
    os = {}
    nowork = {}
    def __init__(self, uch_nom, oborud):
        self.nom = uch_nom
        self.ob = oborud

    @staticmethod
    def sklad_pr(type_sklad):
        if type_sklad =='sklad' or 'os' or 'nowork':
            return True
        print('не верно указан склад  sklad/os/nowork')
        return False

class Printer(Orgteh):
    def to_sklad(self,type_sklad_kuda):
        if Orgteh.sklad_pr(type_sklad_kuda):
            if type_sklad_kuda == 'sklad':
                Orgteh.sklad.update({self.nom:self.ob})
            if type_sklad_kuda == 'os':
                Orgteh.os.update({self.nom:self.ob})
            if type_sklad_kuda == 'nowork':
                Orgteh.nowork.update({self.nom:self.ob})

    def sklad_move(self,type_sklad_ot, type_sklad_kuda):
        if Orgteh.sklad_pr(type_sklad_ot) and Orgteh.sklad_pr(type_sklad_kuda):
            if type_sklad_ot == 'sklad':
                Orgteh.sklad.popitem(self.nom,self.ob)
            if type_sklad_ot == 'os':
                Orgteh.os.popitem(self.nom, self.ob)
            if type_sklad_ot == 'nowork':
                Orgteh.nowork.pop(self.nom,self.ob)
            if type_sklad_kuda == 'sklad':
                Orgteh.sklad.update({self.nom:self.ob})
            if type_sklad_kuda == 'os':
                Orgteh.os.update({self.nom:self.ob})
            if type_sklad_kuda == 'nowork':
                Orgteh.nowork.update({self.nom:self.ob})
        else:
            print('введите верные данные')
class Xerox(Orgteh):
    def to_sklad(self,type_sklad_kuda):
        if Orgteh.sklad_pr(type_sklad_kuda):
            if type_sklad_kuda == 'sklad':
                Orgteh.sklad.update({self.nom:self.ob})
            if type_sklad_kuda == 'os':
                Orgteh.os.update({self.nom:self.ob})
            if type_sklad_kuda == 'nowork':
                Orgteh.nowork.update({self.nom:self.ob})

    def sklad_move(self,type_sklad_ot, type_sklad_kuda):
        if Orgteh.sklad_pr(type_sklad_ot) and Orgteh.sklad_pr(type_sklad_kuda):
            if type_sklad_ot == 'sklad':
                Orgteh.sklad.popitem(self.nom,self.ob)
            if type_sklad_ot == 'os':
                Orgteh.os.popitem(self.nom, self.ob)
            if type_sklad_ot == 'nowork':
                Orgteh.nowork.pop(self.nom,self.ob)
            if type_sklad_kuda == 'sklad':
                Orgteh.sklad.update({self.nom:self.ob})
            if type_sklad_kuda == 'os':
                Orgteh.os.update({self.nom:self.ob})
            if type_sklad_kuda == 'nowork':
                Orgteh.nowork.update({self.nom:self.ob})
        else:
            print('введите верные данные')

class Scaner(Orgteh):
    def to_sklad(self,type_sklad_kuda):
        if Orgteh.sklad_pr(type_sklad_kuda):
            if type_sklad_kuda == 'sklad':
                Orgteh.sklad.update({self.nom:self.ob})
            if type_sklad_kuda == 'os':
                Orgteh.os.update({self.nom:self.ob})
            if type_sklad_kuda == 'nowork':
                Orgteh.nowork.update({self.nom:self.ob})

    def sklad_move(self,type_sklad_ot, type_sklad_kuda):
        if Orgteh.sklad_pr(type_sklad_ot) and Orgteh.sklad_pr(type_sklad_kuda):
            if type_sklad_ot == 'sklad':
                Orgteh.sklad.popitem(self.nom,self.ob)
            if type_sklad_ot == 'os':
                Orgteh.os.popitem(self.nom, self.ob)
            if type_sklad_ot == 'nowork':
                Orgteh.nowork.pop(self.nom,self.ob)
            if type_sklad_kuda == 'sklad':
                Orgteh.sklad.update({self.nom:self.ob})
            if type_sklad_kuda == 'os':
                Orgteh.os.update({self.nom:self.ob})
            if type_sklad_kuda == 'nowork':
                Orgteh.nowork.update({self.nom:self.ob})
        else:
            print('введите верные данные')

pr1 = Printer('001','Xerox')
pr1.to_sklad('nowork')
sc1 = Scaner('002', 'HP')
sc1.to_sklad('os')
xe1 = Xerox('003', 'Xerox')
xe1.to_sklad('sklad')
print(Orgteh.os, Orgteh.sklad, Orgteh.nowork)
pr1.sklad_move('nowork','os')
print(Orgteh.os, Orgteh.sklad, Orgteh.nowork)


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex_num:
    def __init__(self, var):
        self.var = var

    def __add__(self, other):
        i=0
        j=0
        for el in self.var:
            if el != '+':
                i=i+1
            else:
                break
        a=int(self.var[:i])
        b=int(self.var[i+1:-1])
        for el in other.var:
            if el != '+':
                j=j+1
            else:
                break
        c=int(other.var[:j])
        d=int(other.var[j+1:-1])
        res1 = a + c
        res2 = b + d
        return f'{res1}+{res2}i'

    def __mul__(self, other):
        i = 0
        j = 0
        for el in self.var:
            if el != '+':
                i = i + 1
            else:
                break
        a = int(self.var[:i])
        b = int(self.var[i + 1:-1])
        for el in other.var:
            if el != '+':
                j = j + 1
            else:
                break
        c = int(other.var[:j])
        d = int(other.var[j + 1:-1])
        res1 = a * c - b * d
        res2 = b * c + a * d
        return f'{res1}+{res2}i'

v1 = Complex_num('123+10i')
v2 = Complex_num('567+20i')
print(v1+v2)
print(v1*v2)
