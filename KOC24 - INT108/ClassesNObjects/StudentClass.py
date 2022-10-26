class Student:
    def __init__(self, rollNo, name, marks):
        self.rollNo =  rollNo
        self.name = name
        self.marks = marks

    def print(self):
        print(self.rollNo , self.name, self.marks)



#how to create objects of that class
student1 = Student(1, "Ayushi", 25)
student1.print()

student2 = Student(2, "Ashima", 30)
student2.print()

student3 = Student(3, "Mohit", 26)
student3.print()

student4 = Student(4, "Vivek", 30)
student4.print()

student5 = Student(5, "Anu", 30)
student5.print()



# """
# 1. Lengthy - unncessary code lines
# 2. Reduces code readibility
# 3. a lot of variables
# 4. 100 students - 300 variables
# """
# #student1
# roll1 = 1
# name1 = "Ayushi"
# marks1 = 25
#
# #student2
# roll2 = 2
# name2 = "Ashima"
# marks2 = 30
#
# #student3
# roll3 = 3
# name3 = "Mohit"
# marks3 = 27
#
# #student4
# roll4 = 4
# name4 = "Vivek"
# marks4 = 22
#
# #student5
# roll5 = 5
# name5 = "Radhika"
# marks5 = 23
#
