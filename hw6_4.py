class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} машина поехала')

    def stop(self):
        print(f'{self.name} машина остановилась')

    def turn(self):
        print(f'{self.name} машина повернула')

    def show_speed(self):
        print(f'{self.speed} скорость автомобиля')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость выше, чем разрешенной! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} допустима'


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость выше, чем разрешенной! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} допустима'

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        car.__init__(self, name, color, speed, is_police)

police_car = Car('ДПС', 'Белый', 80)
police_car.go()
police_car.stop()
police_car.turn()




