class Car:
    def __init__(self, mileage, topspeed, color):
        self.mileage = mileage
        self.topspeed = topspeed
        self.color = color

    def __str__(self):
        return "mileage is {}, topspeed is {} and color is {}".format(self.mileage, self.topspeed, self.color)

    def getmileage(self):
        print(str(self.mileage)+'mpl')



class Kia(Car):
    def getmileage(self):
        print(str(self.mileage*1.609)+'kmpl')

seltos=Kia(10,20,'Red')
seltos.getmileage()