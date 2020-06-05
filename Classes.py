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

# class Student:
#     def __init__(self, name, stu_num, marks):
#         self.name =  name
#         self.stu_num = stu_num
#         self.marks = marks

#     def __str__(self):
#         return "{} is a student. Their student number is {}. {}'s average mark is {}".format(self.name, self.stu_num, self.name, self.average())

#     def add_mark(self, new_mark):
#         return (self.marks).append(new_mark)

#     def highest_mark(self):
#         return max(self.marks)

#     def lowest_mark(self):
#         return min(self.marks)

#     def average(self,):
#         sum_of_marks = 0
#         for mark in self.marks:
#             sum_of_marks += mark
#         return sum_of_marks/len(self.marks)

# student1 =  Student("Carl", "X1232452", [87,71, 79])
# student2 =  Student("Angela", "X11111452", [65,59, 71])
# student3 =  Student("Rachel", "X1000002", [74,45, 66])

# print(student1.lowest_mark())
# print(student2.name)
# print(student3.average())
# print()
# print(student1.marks)
# print(student1.__str__())
# student1.add_mark(50)
# print("Added new mark to Carls grades:",student1.marks)
# print(student1.__str__())

# ================================================================================================================#
# Design a class to represent a rectangle. Some methods examples can be the rectangle
# area and rectangle perimeter.

# class Rectangle(object):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def perimeter(self):
#         return 2*(self.length + self.width)

#     def area(self):
#         return self.length*self.width

#     def __str__(self):
#         return "Rectangle area is {}. Perimeter is {}.".format(self.area(), self.perimeter())


# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(34, 47)
# print(rect1.area())
# print(rect2.perimeter())
# print(rect2.area())
# print(rect2)

# ================================================================================================================#
# Design a class to represent a bank account. Some information you might want in a bank
# # account are the IBAN, account number, available funds, a list with the last 5 transactions.
# # You might also add methods to withdraw and deposit money.

class BankAccount(object):
    def __init__(self, name='', last_name='', iban='', account_num=0, balance=0):
        self.name = name
        self.last_name = last_name
        self.iban = iban
        self.account_num = account_num
        self.balance = balance
        self.transaction_count = 0
        self.transactions = {}  #Dictionary to store all transactions/info. Keyed by transaction id(count).
        # information will be stored in a tuple (a,b,c,d) where a the type, b is the amount, c is balance
        # after transcation and d is the a message for user to explain transaction e.g. 'bills'.

    def deposit(self, value, message):
        if value < 0:
            print("Cannot deposit a negative value.\n")
            return

        try:
            float_value = float(value)
        except ValueError:
            print("Value entered is not a number. Please enter a correct value.\n")
            return

        self.balance += value
        self.transaction_count += 1
        self.transactions.update({self.transaction_count:("Deposit", value, self.balance, message)})

    def withdraw(self, value, message):
        if value < 0:
            print("Cannot withdraw a negative value.\n")
            return

        try:
            float_value = float(value)
        except ValueError:
            print("Value entered is not a number. Please enter a correct value.\n")
            return

        if value > self.balance:
            print("Value great than current balance. Unable to withdraw funds.\n")
            print("Your current account balance is {}.\n".format(self.balance))
            return

        self.balance -= value
        self.transaction_count += 1
        self.transactions.update({self.transaction_count:("Withdraw", value, self.balance, message)})

    def last_5_transactions(self):
        count = self.transaction_count

        if count < 0:
            print("No transactions have been performed yet.\n")

        printed_transaction = 0
        while count > 0:
            for key, value in self.transactions.items():
                if key == count:
                    print("Transaction : ", value[0])
                    print("Amount : ", value[1])
                    print("Balance : ", value[2])
                    print("Message : ", value[3])
                    print("==========================================================")
            if printed_transaction == 5:
                break
            count -= 1

    def print_balance(self):
        return "Your current balance is ",self.balance

# Lucas account with lots of money
lucas_account = BankAccount(name="Lucas", last_name="Rizzo", iban="IE12345789", balance=1000000)
print(lucas_account.print_balance())

# Transactions
lucas_account.deposit(50000, "bitcoin profit")
lucas_account.withdraw(75000, "casino bet")
lucas_account.withdraw(20000, "trip to bahamas")
lucas_account.withdraw(20000, "money to lawyers")
lucas_account.withdraw(35000, "debt payment")
lucas_account.last_5_transactions()
print(lucas_account.print_balance())

