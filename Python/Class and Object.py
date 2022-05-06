class Car:
    def __init__(self, mileage, topspeed, color):
        self.mileage = mileage
        self.topspeed = topspeed
        self.color = color

    def __str__(self):
        return "mileage is {}, topspeed is {} and color is {}".format(self.mileage, self.topspeed, self.color)


seltos = Car('10', '20', 'black')
print(seltos)
