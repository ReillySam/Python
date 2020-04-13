##### COLLEGE SYSTEM ASSIGNMENT ##### DRAFT 1

# You are asked to develop a small college management system
# to illustrate your understanding of the main object-oriented concepts.
# Your system should keep track of Students. Each student has student ID, name, email address
# and list of current modules they are taking. Each student can enrol in up to 5 modules max.
# Each Module has an unique code, a name, a number of ECTS credits.
# Each module also has a max capacity, and once that is reached no more students can be enrolled until somebody unenrolls first.
# You’ll need to keep track of, and update, what modules are students enrolled in.
# Some of the functionality your system should provide is:
#     • Print and update details about the students
#     • Print and update details about the modules
#     • Search for a student using different parameters (e.g. by email or student ID)
#     • Enrol and unenroll a student from a module
#     • Create and delete students and modules

# ASSOCIATED DICTIONARIES. GET/SET METHODS. PACKING AND UNPACKING. ZIP FUNCTION TO PAIR ITEMS OF RELATED LISTS
# LIST/GENERATOR COMPREHENSIONS. DECORATORS. *ARGS & **KWARGS - some things i was looking at and wana
# try implement (if possible) to understand more etc etc

# I know there's a handfull of stuff that wont work, just need to put this aside for the next couple days
# confused on how methods will behave together. are they called automatically in some cases or does they need to be called
# from other classes and other methods

# Modules object used to define each module. A Composition relationship type with ModuleOffering
class Module:

    def __init__(self, module_code, module_name, ects_credits, capacity):
        '''Initialising Module attributes'''
        self.module_code = module_code
        self.module_name = module_name
        self.ects_credits = ects_credits
        self.capacity = capacity

    def increase_capacity(self, enroll_count):
        '''Increase the module capacity if a student enrolls'''
        enroll_count = self.capacity + 1
        return enroll_count

    def decrease_capacity(self, enroll_count):
        '''Decrease the modules capacity if a student un-enrolls'''
        enroll_count = self.capacity - 1
        return enroll_count

    @classmethod
    def module_input(cls): ##Validation arguments needed
        '''Take user inputs to create new module details'''
        module_name = input("Enter Module name: ")
        module_code = input("Enter Module code: ")
        ects_credits = 0
        capacity = 0
        while 1:
            try:
                ects_credits = int(input("Enter Modules ECTS Credits: "))
                capacity = int(input("Enter the modules current capacity: "))
            except ValueError:
                print("Invalid input")
            return cls(module_name, module_code, ects_credits, capacity)

    def __repr__(self):
        '''Display module information''' # a lot of sources say these are needed but i feel like im repeating myself? proabbaly not using it right
        return "Module - {}: {}: {} ECTS Credits: {} enrolled".format(self.module_code, self.module_name,
                                                                      self.ects_credits, self.capacity)

    def __str__(self):
        '''Display module details in a string for user'''
        return "{} : {}. This module carries {} ETCS Credits. Current capacity is {}.".format(self.module_name, self.module_code,
                                                                                    self.ects_credits, self.capacity)

# ================================================================================================================#
# Student is to define each student and their details, modules list, enroll and un-enroll students
class Student:

    def __init__(self, stud_id, stu_name, email):
        '''Initialising Student attributes'''
        self.stud_id = stud_id
        self.student_name = stu_name
        self.email = email
        self.module_list = []

    @property
    def set_email(self): #I dont need to initialise email in this case? but then how to call it/print in __str__/__repr__ or is only in instances
        '''set student email format'''
        return "{}@collegeEmail.com".format(self.stud_id)

    def __len__(self):
        '''Get the length of students module list'''
        return len(self.module_list)

    def set_module_list(self):
        '''Add a module to students module list'''
        try:
            while self.module_list <= 5:
                self.module_list += 1
                return
        except ValueError:
            return "{} has reached their maximum module count".format(self.student_name)

    @classmethod
    def student_input(cls):  ##Validation arguments needed
        '''Take user inputs to create new student details'''
        while 1:
            try:
                student_name = input("Enter Student name: ")
                stud_id = input("Enter Student ID: ")
                email = input("Enter a valid email: ")
                return cls(student_name, stud_id, email)
            except ValueError:
                return "Invalid input"

    def __repr__(self):
        '''Display Student details'''
        return "Student - {}: ", "{}: ", "{}:  \n" "{}".format(self.stud_id, self.student_name, self.email, self.module_list)

    def __str__(self):
        '''Display Student details in a string for users'''
        print ("{} : {}, is taking the following modules.\n".format(self.stud_id, self.student_name))
        return [mod for mod in self.module_list]

# ================================================================================================================#
# Schools object used to define departments that house certain modules and relevant students
# Would __iter__ be good here to iterate across dicts and not repeatedly use for loops?
class School:

    def __init__(self, school_name):
        '''Initialising School and its attributes'''
        self.school_name = school_name
        self.module = {}
        self.student = {}

    def get_module_item(self, key):
        '''get the module from module dictionary'''
        if isinstance(key, str):
            return self.module[key]
        raise TypeError ("Cannot find module : {}.".format(self.module[key]))

    def get_student_item(self, key):
        '''get the student from student dictionary'''
        if isinstance(key, str):
            return self.student[key]
        raise TypeError ("Cannot find student : {}.".format(self.student[key]))

    def __contains__(self, key):
        '''Checks the key in a dictionary is present if 'in' function is called'''
        return key in self.module or self.student

    def enrollment(self, student):
        '''enroll a student in a module'''
        try:
            while len(enroll_count) <= 10:
                return self.module.update(student)
        except ValueError:
            return "Sorry, this module is full."

    def disenroll(self, student):
        '''disenroll a student from a module'''
        self.module.pop(student)
        return "{} has been un-enrolled from.".format(student)

    def add_module(self, module_code, module_name, ects_credits, capacity):
        '''create a new module'''
        newModule = Module(self, module_code, module_name, ects_credits)
        try:
            if self.module[module_code] in self.module.items():
                print("This is already a module, see module code {}.").format(self.module[module_code])
                raise ValueError
        except Exception:
            mod_details = [module_name, ects_credits, capacity]
            self.module[module_code] = mod_details
            return self.module.update()

    def add_student(self, stud_id, stud_name, email):
        '''create a new student'''
        new_student = Student(self, stud_id, stud_name)
        try:
            if new_student in self.student.items():
                print("This student already exits, {} : {}").format(self.student[stud_id], self.student[stud_name])
                raise ValueError
        except Exception:
            stu_details = [stud_name, email]
            self.student[stud_id] = stu_details
            return self.student.update()

    def delete_module(self, module_code):
        '''delete a module'''
        try:
            if module_code not in self.module.keys():
                print("This module doesnt exist.")
                raise TypeError
        except Exception:
            return self.module.pop([module_code])

    def delete_student(self, stud_id):
        '''delete a student'''
        try:
            if stud_id not in self.student.keys():
                print("This student doesnt exist.")
                raise TypeError
        except Exception:
            return self.module.pop([stud_id])

    def search_student(self, search):
        '''search for a student using student id or student email'''
        self.stud_id = 0
        self.email = ''
        for item in self.student.items():
            self.stud_id = item[0]
            self.email = item[1][1]
        try:
            if self.stud_id == search or self.email == search:
                return Student(self.stud_id, self.school_name, self.email)
        except Exception:
            raise ValueError("{} ia an invalid input.".format(search))

    def __repr__(self):
        '''Display all module college information'''
        return {key: value for key, value in self.module.items()}

    def __str__(self):
        '''Display all college information in a string for users'''
        print("The School of {} offers the following modules. \n".format(self.school_name))
        return {key:value for key,value in self.module.items()}

# ================================================================================================================#
# Some Instantiations
soc = School("School of Computing")

mod1 = Module("CMPZ163", "System Analysis and Testing", 5, 10)
mod2 = Module("CMPY999", "Information Systems", 5, 10)
mod3 = Module("CMPX001", "OO Software Development", 10, 10)

stu1 = Student("X001200", "Joe Soap", "email@college.com")
stu2 = Student("X100001", "Frank Smith", "newemail@college.com")
stu3 = Student("X123120", "Rachel Anderson", "lastemail@college.com")

print(mod1.module_code)
print(mod3.module_name)
soc.delete_module("CMPY999")
soc.__repr__()

Module.module_input()
Student.student_input()
