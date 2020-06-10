#INTRODUCTION

#We know that there are OBJECTS of certain classes in python
#x='hello'
#print(type(x))
#y=3
#print(type(x))



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print(name)
    def add_one(self, x, y):
        return x+y+1
    def bark(self):
        print("bark")
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

d = Dog("Tim", 13)
d.set_age(23)
print(d.get_name(),d.get_age())
#d.bark()
#print(d.add_one(5,3))
#print(type(d))

dog1_name = "Tim"
dog1_age = 34