class Dog:
    def __init__(self, color, breed): #constructor  --- it is called automatically when object is created
        #instance variables- variables which are specific to each object
        self.color = color
        self.breed = breed

    def print(self, color, breed): #self contains address of that object
        print(color, self.breed)

d1=Dog("brown", "boxer")
d2=Dog("xyz", "abc")
d3=Dog("black", "hij")
d4=Dog("light brown", "golden retriever")
d5=Dog("grey", "def")

l=[d1,d2,d3,d4,d5] #list of objects

for i in l:
    print(i.color, i.breed)
