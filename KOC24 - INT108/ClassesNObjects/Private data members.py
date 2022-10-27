class Dog:
    #class variable
    animal = "dog"

    def __init__(self, breed, color):
        #instance variables
        self._breed = breed #public
        self._color = color #public - outside the class can be accessed
        #private  -- can be accessed only inside the class not outside the class

    def func(self):
        print(self._breed, self._color)

rodger = Dog("Pug", "brown")
buzo = Dog("Bulldog", "black")
rodger.func()
