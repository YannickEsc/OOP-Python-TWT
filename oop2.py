#NOW LETS TALK A LITTLE BIT ABOUT INHERITANCE

class Pet:  #GENERALIZATION
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet): #SPECIFIC CLASS
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I'm color {self.color}")

class Dog(Pet): #SPECIFIC CLASS 
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "blue")
c.show()
#c.speak()
d = Dog("Joe", 25)
d.show()
#d.speak()
f = Fish("Bubbles", 10)
f.speak()