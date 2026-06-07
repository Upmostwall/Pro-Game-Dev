class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")

my_dog = Dog("Buddy", "Labrador")
my_dog.bark()
