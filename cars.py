class Car:
    def _init_(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand}'s speed is now {self.speed}")

mycar = Car("Bugatti", 240)
mycar.accelerate()
mycar.accelerate()
mycar.accelerate()
mycar.accelerate()
mycar.accelerate()

mycar2 = Car("Lamborghini" 210)
mycar2.accelerate()
mycar2.accelerate()
mycar2.accelerate()

