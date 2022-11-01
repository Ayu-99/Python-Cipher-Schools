class Dog:
    #class variable
    animal = "dog"

    def __init__(self, breed, color):
        #instance variables
        self.breed = breed
        self.color = color

rodger = Dog("Pug", "brown")
buzo = Dog("Bulldog", "black")

print(Dog.animal, rodger.breed, rodger.color, rodger.animal)
print(Dog.animal, buzo.breed, buzo.color, buzo.animal)

#class variables can be accessed using class name or object
#instance variables can only be accessed using object


"""
Instance variables are variables whose value is assigned isnide a class
inside a constructor or a function, whereas the class variables are 
variables whose value is assigned inside the class.
Instance variables are for data unique to each object/instance
class variables are shared by all instances.
""
