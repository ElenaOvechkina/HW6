class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 30
        self.height = 7
    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна необходимо {round(asphalt_mass)} массы асфальта')


r = Road(10000, 60)
r.asphalt_mass()