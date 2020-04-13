#INHERITANCE 

##Inheritance examples show deriving new sub classes from a parent class
##A combination of generalisation and specialisation

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
# class Student(Person):
#     def __init__(self, name, age, stud_num, course):
#         Person.__init__(self, name, age)
#         self.stud_num = stud_num
#         self.course = course
#
#
#
# class Staff(Person):
#     def __init__(self, name, age, staff_num, office_num):
#         Person.__init__(self, name, age)
#         self.staff_num = staff_num
#         self.office_num = office_num
#
#
#
# student1 = Student("Jack", 22, "D0903", "Engineering")
# student2 = Student("Amy", 21, "D3424", "Accounting")
#
# staff1 = Staff("Frank", 44, "E112", 121)
# staff2 = Staff("Patrick", 39, "E041", 54)
#
# print(student1.course)
# print(student2.name)
# print()
# print(staff1.office_num)
# print(staff2.staff_num)


# -------------------------------------------------
# Write a class Bank. Every bank has a name, a list of savings accounts,
# and a list of current accounts.
# SavingsAccount has an interest rate and a method to calculate interest.
# CurrentAccount has an overdraft.

class BankAccount:
    def __init__(self, acc_number, balance):
        self._acc_number = acc_number
        self._balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, acc_n, balance, interest_rate):
        BankAccount.__init__(self, acc_n, balance)
        self._int_rate = interest_rate

    def __str__(self):
        return "#"+self._acc_number+" balance: "+str(self._balance) + " int rate: " + str(self._int_rate)


class CurrentAccount(BankAccount):
    def __init__(self, acc_n, balance, overdraft):
        BankAccount.__init__(self, acc_n, balance)
        self._overdraft = overdraft

    def __str__(self):
        return "#"+self._acc_number+" balance: "+str(self._balance) + " overdraft: " + str(self._overdraft)


class Bank():
    def __init__(self, name, c_accounts, s_accounts):
        self._name = name
        self._current_accs = c_accounts
        self._saving_accs = s_accounts

    def add_current_account(self, c_acc):
        self._current_accs.append(c_acc)

    def print_bank(self):
        print(self._name)

        print("Current accounts:")
        for a in self._current_accs:
            print(a)

        print("Saving accounts:")
        for a in self._saving_accs:
            print(a)

bank = Bank("BOI", [CurrentAccount("1111", 1000.00, 200.00)], [SavingsAccount("2222", 2000.00, 5.1)])
bank = Bank("BOI", [], [SavingsAccount("2222", 2000.00, 5.1), SavingsAccount("2223", 2020.00, 5.5)])
bank.print_bank()

print()
bank.add_current_account(CurrentAccount("1112", 1200.00, 300.00))
bank.print_bank()
