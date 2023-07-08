class Vehicle:
    def __init__(self, name, shape, technology):
        self.name = name
        self.shape = shape
        self.technology = technology

    def getname(self):
        return self.name

    def getShape(self):
        return self.shape

    def getTechnology(self):
        return self.technology


class Airplane(Vehicle):
    def __init__(self, name, shape, technology, seatingCapacity):
        super().__init__(name, shape, technology)
        self.seatingCapacity = seatingCapacity

    def getSeatingCapacity(self):
        return self.seatingCapacity


class Boat(Vehicle):
    def __init__(self, name, shape, technology, knotsVelocity, travelDistance):
        super().__init__(name, shape, technology)
        self.knotsVelocity = knotsVelocity
        self.travelDistance = travelDistance

    def gettravelDistance(self):
        return self.travelDistance


# Instantiate a new object from Airplane that inherits from Vehicle

boeing = Airplane("Boeing 727", "Linear", "Hybrid", 300)
print('Boing Vehicle has ' + str(boeing.getSeatingCapacity()) + ' seats ')
print('Boeing Vehcile nas name of: ', boeing.getname())
print('Boeing is class of ', type(boeing))
