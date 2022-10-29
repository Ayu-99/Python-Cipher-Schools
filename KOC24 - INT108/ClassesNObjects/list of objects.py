class Student:
    subject="maths"  #class variable
    def __init__(self, id, name, marks):  #constructor- it is automatically called when obejct is created
        #instance variables
        self.id = id
        self.name = name
        self.marks = marks

    def print(self): #self stores the address of the object
        print(self.id, self.name, self.marks)

#assignment operator - right to left
s1 = Student("1", "Ayushi", 25)
s2 = Student("2", "Ashima", 30)
s3 = Student("3", "Mohit", 35)
s4 = Student("4", "Vivek", 49)
s5 = Student("5", "Vidushi", 50)

# print(s1)
# s1.print()  # print(s1)
l=[s1,s2,s3,s4,s5] #list of objects

for i in l:
    print(i.id, i.name, i.marks)
