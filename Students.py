class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")

student1 = Student("Bob", 21)
student1.introduce()

student2 = Student("Will" 21)
student2.introduce()

