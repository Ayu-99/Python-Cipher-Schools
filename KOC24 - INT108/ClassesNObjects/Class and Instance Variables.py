class Dog:
    x = "mammal" #class variables - they can be accessed outside the class with class name
    y = "dog"
    def __init__(self):
        #instance variables
        self.animal = "yes"

    def fun(self):
        print("I am a ", self.x)
        print("I am a ", self.y)

d = Dog()
print(Dog.x, Dog.y, d.animal)
d.fun()



