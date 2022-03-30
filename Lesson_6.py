# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
#
# простой способ организации светофора :) с бесконечным циклом
from time import sleep
from itertools import cycle
color = ['red', 'yellow', 'green', 'yellow']
ltime = [7,3,7,3]
for a in cycle('0123'):
    i = int(a)
    print(color[i])
    sleep(ltime[i])


#
# по заданию
from time import sleep
from itertools import cycle
class Trafficlight:
    color = ['red', 'yellow', 'green', 'yellow']
    def running(self,c):
        self.__i = c
        return f'{Trafficlight.color[self.__i]}'

sf=Trafficlight()
ltime = [7,3,7,3]
for a in cycle('0123'):
    i = int(a)
    print(sf.running(i))
    sleep(ltime[i])

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
#

class Road:
    m1 = 25
    def massa(self):
        return self._l * self._w * Road.m1 * self.s / 1000
    def __init__(self,lenght, widht, sm):
        self._l = lenght
        self._w = widht
        self.s = sm

lenght_road = int(input('Длинна дороги в м: '))
widht_road = int(input('ширина дороги в м: '))
cm_road = int(input('Толщина покрытия в см: '))
road = Road(lenght_road,widht_road, cm_road)
print(road.massa(), "T")


#
# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
#

# #
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage, 'bonus':bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_full_income(self):
        summa = self._income.get('wage') + self._income.get('bonus')
        return summa


spisok_sotr = []
i=0
while True:
    a=[] # промежуточный список для формирования данных по каждому сотруднику
    if input('Для ввода следующей позиции нажмите Enter, для остановки ввода s: ') == 's':
        break
    name = input('введите Имя: ')
    surname = input('введите Фамилию: ')
    position = input('введите занимаемую должность')
    try:
        wage = int(input('введите оклад: '))
        bonus = int(input('введите размер бонуса: '))
    except ValueError:
        print('введите оклад и бонус в виде целого числа')
        wage = int(input('введите оклад: '))
        bonus = int(input('введите размер бонуса: '))

    pos = Position(name, surname, position, wage, bonus)

    # print(pos.get_full_name(), pos.get_full_income()) # для проверки промежуточных обращений
    a = pos.get_full_name().split()
    a.append(pos.get_full_income())
    spisok_sotr.append(a) #создается список списков сотрудников

for i in range(len(spisok_sotr)):
    print(spisok_sotr[i])



#
# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
#
class Car:
    def __init__(self, name, color, speed, is_police):
         self.speed = speed
         self.color = color
         self.name = name
         self.is_police = bool(is_police)

    def show_speed(self):
         print(self.color, ' ', self.name, ' ',self.speed)
    def go(self):
         print(f'машина {self.color} {self.name} едет')
    def stop(self):
         print(f'машина {self.color} {self.name} остановлена')
    def turn(self, direction):
         self.direction = direction
         print(f'машина {self.color} {self.name} едет {self.direction}')
    def police(self):
        print(f'Машина {self.color} {self.name} в розыске') if bool(self.is_police) else print(f'Машина {self.color} {self.name} не в розыске')

class TownCar(Car):
    def show_speed(self, nspeed=None):
        if nspeed == None:
            print(self.color, ' ', self.name,' ',self.speed)
        else:
            if nspeed > 60:
                print(self.color, ' ', self.name,'превышение скорости на ',nspeed - 60,'  скорость  ', nspeed)
            else:
                print(self.color, ' ', self.name, ' ', nspeed)
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self,nspeed=None):
        if nspeed == None:
            print(self.color, ' ', self.name, ' ', self.speed)
        else:
            self.speed = nspeed
            if self.speed > 40:
                print(self.color, ' ', self.name,'превышение скорости на ',self.speed - 40,'  скорость  ', nspeed)
            else:
                print(self.color, ' ', self.name, ' ',self.speed)

t_car1 = TownCar('Volvo','red',30, False)
s_car1 = SportCar('Subaru', 'blue', 100, False)
w_car1 = WorkCar('GAZ', 'Orange', 20, False)
t_car2 = TownCar('Nissan', 'grey', 40, False)
s_car2 = SportCar('Mitsubishi', 'silver', 80, False)
t_car3 = TownCar('Nissan', 'green', 50, True)
t_car1.show_speed(70)
s_car2.show_speed()
s_car2.go()
t_car1.turn('напрaво')
t_car3.police()
w_car1.show_speed()



#
# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки ', self.title)

class Pen(Stationery):
    def draw(self):
        print("рисование ручкой ", self.title)
class Pencil(Stationery):
    def draw(self):
        print('рисование карандашом ', self.title)
class Handle(Stationery):
    def draw(self):
        print('рисование маркером ', self.title)

pen1 = Stationery('pen 1')
pen2 = Pen('pen 2')
penc1 = Stationery('pencil 1')
penc2 = Pencil('pencil 2')
han1 = Stationery('handle 1')
han2= Handle('handle 2')

pen1.draw()
pen2.draw()
penc1.draw()
penc2.draw()
han1.draw()
han2.draw()