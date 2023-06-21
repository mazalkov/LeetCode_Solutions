class ParkingSystem():

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.lookup = [self.big, self.medium, self.small]

    def addCar(self, carType: int) -> bool:
        label = self.lookup[carType-1]
        if label > 0:
            self.lookup[carType-1] -= 1
            return True
            
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
