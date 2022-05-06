class Car:
    def __init__(self, mileage, topspeed, color):
        self.mileage = mileage
        self.topspeed = topspeed
        self.color = color

    def __str__(self):
        return "mileage is {}, topspeed is {} and color is {}".format(self.mileage, self.topspeed, self.color)

    def getmileage(self):
        print(self.mileage)



class Kia(Car):
    pass

seltos=Kia(10,20,'Red')
seltos.getmileage()