## Examples + short exercise
# -------------------------------------------------
# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def __str__(self):
#         return "{} is {} years of age and lives at {}".format(self.name, self.age, self.address)
#
#     def age_diff(self, some_person):
#         return self.age - some_person.age
#
#     def is_older(self, some_person):
#         if self.age - some_person.age >= 1:
#             return True
#         else:
#             return False
#
#
# per1 = Person("John", 35, "12 Pike st.")
# per2 = Person("Mary", 35, "121 Martyr Avenue.")
# per3 = Person("Linda", 46, "Cast adrift way.")
#
# print(per1.is_older(per2))
# print(per2.age_diff(per1))
# print(per2.name)
# print(per1.__str__())

# -------------------------------------------------
##Write a class student. Every student has a name, stu number and a list of their marks.
##Include any appropriate methods and a method to calculate average mark

class Student:
    def __init__(self, name, stu_num, marks):
        self.name =  name
        self.stu_num = stu_num
        self.marks = marks

    def __str__(self):
        return "{} is a student. Their student number is {}. {}'s average mark is {}".format(self.name, self.stu_num, self.name, self.average())

    def add_mark(self, new_mark):
        return (self.marks).append(new_mark)

    def highest_mark(self):
        return max(self.marks)

    def lowest_mark(self):
        return min(self.marks)

    def average(self,):
        sum_of_marks = 0
        for mark in self.marks:
            sum_of_marks += mark
        return sum_of_marks/len(self.marks)

student1 =  Student("Carl", "X1232452", [87,71, 79])
student2 =  Student("Angela", "X11111452", [65,59, 71])
student3 =  Student("Rachel", "X1000002", [74,45, 66])

print(student1.lowest_mark())
print(student2.name)
print(student3.average())
print()
print(student1.marks)
print(student1.__str__())
student1.add_mark(50)
print("Added new mark to Carls grades:",student1.marks)
print(student1.__str__())
