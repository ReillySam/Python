##Examples and Exercises of Aggregation and Composition
## Aggregation
'''this type of relationship implies that the child class can exist
independently of its parent class'''

##Parent class in this scenario is Module, Person being the child or sublcass.
##it is able to exit without needing the Module class

class Module:
    def __init__(self, name):
        self._name = name
        self._students = []

    def get_name(self):
        return self._name

    def add_student(self, new_stu):
        self._students.append(new_stu)

    def get_student(self):
        return self._students

    def print_students(self):
        if self._students == []:
            print("No Students")

        else:
            for i in range(len(self._students)):
                print(self._students[i])

class Person():
    def __init__(self, name , age, address):
        self._name = name
        self._age = age
        self._address = address

    def __str__(self):
        return "Person: {} + Age: {}".format(self._name, self._age)


per1 = Person("John", 34, "3 The Green")
per2 = Person("Anne", 29, "Avenue Moore")
per3 = Person("David", 20, "Willow Park")

m = Module("OOSD")
m.add_student(per1)
m.add_student(per2)

mod1 = Module("Systems Analysis")
mod1.add_student(per3)

print("Course: "+ m.get_name())
print("Course: "+ mod1.get_name())

m.add_student(Person("Scott", 22, "Westpark 6"))

print("Students: "+ m.get_student())
m.print_students()
mod1.print_students()


# -------------------------------------------------
# We-write the shapes classes from couple of weeks ago and
# instead of using two numbers, x and y, for the coordinates of
# the share, use an object of class Point instead.

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#     def set_x(self, new_x):
#         self._x = new_x
#
#     def set_y(self, new_y):
#         self._y = new_y
#
#     def __str__(self):
#         return "("+str(self._x)+","+str(self._y)+")"
#
#
# class Circle(object):
#     def __init__(self, p, radius):
#         self._center = p
#         self._radius = radius
#
#
#     def move(self, new_x, new_y):
#         self._center.set_x(new_x)
#         self._center.set_y(new_y)
#
#     def __str__(self):
#         return "Circle with center:" + str(self._center) + " and radius "+ str(self._radius)
#
# c1 = Circle(Point(1,1), 3)
# print(c1)
#
# c1.move(2,2)
# print(c1)




# Write a class to represent a Salary – salary object has monthly pay amount and a yearly bonus.
# Add a method to calculate annual pay.Write a class for Employee – each employee has a name, age and a salary
# (use your salary class). Add any necessary methods.Write a class Company – each company has a name and a list
# of employees. Add a method to calculate the total pay to all employees per year. Add a functionality
# to increase everybody’s monthly pay by 5%, and calculate the total pay for the company again.

class Salary:
    def __init__(self, pay=0):
        self._pay = pay

    def increase_pay(self):
        self._pay = self._pay * 1.05

    def get_bonus(self):
        return self.annual_salary() - self.yearly_bonus()

    def annual_salary(self):
        annual_pay = self._pay*12
        return annual_pay

    def yearly_bonus(self):
        return self.annual_salary()*1.2

    def __str__(self):
        return "Pay: ", self._pay, "Annual Salary: ", self.annual_salary(), "Salary + Bonus: ", self.yearly_bonus()

class Employee(object):
    def __init__(self, name, pay):
        self._name = name
        self._pay = pay
        self._obj_salary = Salary(self._pay)

    def employee_earnings(self):
        return self._obj_salary.yearly_bonus()

    def increase_pay(self):
        self._obj_salary.increase_pay()

    def __str__(self):
        return self._name + " earns " + str(self.employee_earnings())

class Company(object):
    def __init__(self, name=""):
        self.name = name
        self.employees = []

    def add_employee(self, name, pay):
        employee = Employee(name, pay)
        self.employees.append(employee)

    def total_salaries(self):
        total = 0
        for e in self.employees:
            total += e.employee_earnings()
        return total

    def increase_all_pay(self):
        for e in self.employees:
            e.increase_pay()

    def print_all_employees(self):
        for e in self.employees:
            print(e)


ibm = Company("IBM")
ibm.add_employee("Mark", 2500)
ibm.add_employee("Sam", 3500)
ibm.add_employee("Harry", 2750)

print(ibm.print_all_employees())
print(ibm.total_salaries())
print()
print("Increasing pay....")
ibm.increase_all_pay()
print()
print(ibm.print_all_employees())
print(ibm.total_salaries())
