##Encaspluation methods, use of privacy for methods and attributes
## to keep these operations internal to the object
## i.e. Making surname private


class Person:

    def __init__(self, firstName, surName, age):
        self.firstName = firstName
        self.__surName = surName
        self.age = age

    def get_firstName(self):
        return self.firstName

    def get_surName(self):
        return self.__surName

    def get_age(self):
        return self.age

person1 = Person("John", "Smith", 57)
person2 = Person("Ann", "Waye", 48)
person3 = Person("Greg", "Ryder", 23)

print(person1.get_firstName())
print(person2.get_surName())

people = [person1, person2, person3]
for i in people:
    print(i.get_firstName())

#populatin a list and iterating through it
people = []

for i in range(3):
    firstName = input("Enter the first name: ")
    surName = input("Enter the surname: ")
    age = int(input("Enter a age: "))
    p = Person(firstName, surName, age)
    people.append(p)

for p in people:
    print(p.get_firstName())
    print(p.get_surName())
    print(p.get_age())

# -------------------------------------------------
### Develop and implement a clock system that measures hours, minutes and seconds.
import time

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self. seconds = seconds

        while True:
            print (str(self.hours).zfill(2),":", str(self.minutes).zfill(2), ":", str(self.seconds).zfill(2))
            self.seconds += 1
            time.sleep(1)
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1

            elif self.minutes == 60:
                self.minutes = 0
                self.hours += 1

            elif self.hours == 24:
                self.hours = 0
                self.minutes = 0
                self.seconds = 0


time = Clock(23, 59, 57)
print(time.tell_time())
