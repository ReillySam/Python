                                        ##### COLLEGE SYSTEM ASSIGNMENT #####
'''
    You are asked to develop a small college management system
    to illustrate your understanding of the main object-oriented concepts.
    Your system should keep track of Students. Each student has student ID, name, email address
    and list of current modules they are taking. Each student can enrol in up to 5 modules max.
    Each Module has an unique code, a name, a number of ECTS credits.
    Each module also has a max capacity, and once that is reached no more students can be enrolled until somebody unenrolls first.
    You’ll need to keep track of, and update, what modules are students enrolled in.
    Some of the functionality your system should provide is:
        • Print and update details about the students
        • Print and update details about the modules
        • Search for a student using different parameters (e.g. by email or student ID)
        • Enrol and unenroll a student from a module
        • Create and delete students and modules

    ASSOCIATED DICTIONARIES. GET/SET METHODS. PACKING AND UNPACKING. ZIP FUNCTION TO PAIR ITEMS OF RELATED LISTS
    LIST/GENERATOR COMPREHENSIONS. DECORATORS. *ARGS & **KWARGS - some things i was looking at and wana
    try implement (if possible) to understand more etc etc. I know most wont apply here
'''

# Modules object used to define each module.
class Module:

    num_of_modules = 0

    def __init__(self, module_code, module_name, ects_credits, students=None):
        '''Initialising Module attributes'''
        self.module_code = module_code
        self.module_name = module_name
        self.ects_credits = ects_credits

        if students is None:
            self.student_list = []
        else:
            self.student_list = students

        #Module.num_of_modules += 1  # count the number of modules

    @property
    def get_module(self):
        '''Get the module name'''
        return self.module_name

    @property
    def get_code(self):
        '''Get the module code'''
        return self.module_code

    @property
    def get_capacity(self):
        '''Get the capacity of the module'''
        return len(self.student_list)

    @property
    def get_student_list(self):
        '''Get the list of students'''
        return self.get_student_list

    @get_student_list.setter
    def get_student_list(self, student):
        '''Add a student to the module's student list'''
        try:
            while self.get_capacity <= 10:
                self.student_list.append(student)
        except ValueError:
            print("{} has reached its maximum capacity.".format(self.module_name))

    def increase_capacity(self):
        '''Increase the module capacity when a student enrolls'''
        self.student_list = int(self.student_list + 1)

    def decrease_capacity(self):
        '''Decrease the modules capacity when a student un-enrolls'''
        self.student_list = int(self.student_list - 1)

    def module_input(self): ##Needs Validation checks, also had this as a classmethod initially, but ran into trouble calling it outisde the class
        '''Take user inputs to create new module details'''
        module_name = input("Enter Module name: ")
        module_code = input("Enter Module code: ")
        ects_credits = 0
        student_list = []
        while 1:
            try:
                ects_credits = int(input("Enter Modules ECTS Credits: "))
                student_list = int(input("Enter the modules current capacity: "))
            except ValueError:
                print("Invalid input")
            return module_name, module_code, ects_credits, student_list

    def __repr__(self):  # a lot of sources say these are needed but i feel like im repeating myself? probably not using it right
        '''Display module information'''
        return "Module - {}: {}: {} ECTS Credits: {} students enrolled".format(self.module_code, self.module_name,
                                                                      self.ects_credits, self.get_capacity)

    def __str__(self):
        '''Display module details in a string for user'''
        return "{} : {}. This module carries {} ETCS Credits. Current capacity is {}.".format(self.module_name, self.module_code,
                                                                                    self.ects_credits, self.get_capacity)

# ================================================================================================================#
# Student is to define each student and their details, modules list, enroll and un-enroll students
class Student:

    num_of_students = 0

    def __init__(self, stud_id, stu_name, modules=None):
        '''Initialising Student attributes'''
        self.stud_id = stud_id
        self.student_name = stu_name

        if modules is None:
            self.module_list = []
        else:
            self.module_list = modules

        #Student.num_of_students += 1  #count the number of students

    @property
    def get_name(self):
        '''Get the students name'''
        return self.student_name

    @property
    def get_id(self):
        '''Get the students id'''
        return self.stud_id

    @property
    def set_email(self):
        '''Set student email format'''
        return "{}@collegeEmail.com".format(self.stud_id)

    @property
    def module_count(self):
        '''Get the length of students module list'''
        return len(self.module_list)

    @property
    def get_module_list(self):
        return self.module_list

    @get_module_list.setter
    def get_module_list(self, module):
        '''Add a module to students module list'''
        try:
            while self.module_count <= 5:
                self.module_list.append(module)
        except ValueError:
            print("{} has reached their maximum module count".format(self.student_name))

    def student_input(self):  ##Validation needed, same as module class
        '''Take user inputs to create new student details'''
        while 1:
            try:
                student_name = input("Enter Student name: ")
                stud_id = input("Enter Student ID: ")
                return student_name, stud_id
            except ValueError:
                return "Invalid input"

    def __repr__(self):
        '''Display Student details'''
        return "Student - {}: ", "{}: ", "{}:  \n" "{}".format(self.stud_id, self.student_name,
                                                               self.set_email, self.module_list)

    def __str__(self):
        '''Display Student details in a string for users'''
        print ("{} : {}, is taking the following modules.\n".format(self.stud_id, self.student_name))
        return [mod for mod in self.module_list]

# ================================================================================================================#
# Schools object used to define departments that house certain modules and relevant students
# Would an __iter__  method be good here to iterate across dicts and not repeatedly use loops?
class School:

    def __init__(self, school_name):
        '''Initialising School and its attributes'''
        self.school_name = school_name
        self.module = {}
        self.student = {}

    def __contains__(self, key):  ## not sure on this, was using it with isinstance (but took them out)
        '''Checks the key in a dictionary is present if 'in' function is called'''
        return key in self.module or self.student

    def find_module(self, code):  # need a error handling here?
        '''Find and call the module code'''
        return {key: value for key, value in self.module.items() if Module.get_code == code}

    def find_student(self, id):
        '''Find and call the student id'''
        return {key: value for key, value in self.student.items() if Student.get_id == id}

    def enrollment(self):
        '''enroll a student in a module'''
        student_id = input("Please enter the student ID: ")
        module_code = input("Please enter the module code: ")

        student = self.find_student(student_id)
        module = self.find_module(module_code)
        try:
            while True:
                module.set_student_list(student)
                student.set_module_list(module)
                print("{} has successfully enrolled.".format(student))
                return Module.increase_capacity
        except ValueError:
            return "Student capacity/module limit reacheds."

    def disenroll(self, id):
        '''disenroll a student from a module'''
        student = self.find_student(id)
        try:
            if student not in Module.get_student_list:
                print("{} does not appear to be in enrolled in {}.").format(student, Module.get_module)
        except:
            self.module.pop(student)
            print("{} has been un-enrolled from.".format(student))
            return Module.decrease_capacity

    def add_module(self, module_code, module_name, ects_credits, student_list):
        '''create and add a module'''
        new_module = Module.module_input  ##Trying to call the module_input from Module. Should it be inside try/except or?
        #new_module = Module(module_code, module_name, ects_credits) # this is what i origianlly had
        try:
            if new_module in self.module.items():
                print("This is already a module, see module code {}.").format(self.module[module_code])
                raise ValueError
        except:
            # make module code the key and the mod details the list of its values
            mod_details = [module_name, ects_credits, student_list]
            self.module[module_code] = mod_details
            return self.module.update(new_module)

    def delete_module(self, code):
        '''delete a module'''
        mod = self.find_module(code)
        try:
            if mod not in self.module.keys():  # is searching by keys better here, or self.module.items()?
                print("This module doesnt exist.")
                raise TypeError
        except:
            print(self.module[code], " is successfully deleted.")
            return self.module.pop([code])

    def add_student(self, stud_id, stu_name):
        '''create and add a student'''
        new_student = Student.student_input
        #new_student = Student(stud_id, stu_name)
        try:
            if new_student in self.student.items():
                print("This student already exits, {} : {}").format(self.student[stud_id], self.student[stu_name])
                raise ValueError
        except Exception:
            stu_details = [stu_name, self.set_email]  ##email has a set email property
            self.student[stud_id] = stu_details
            return self.student.update(new_student)

    def delete_student(self, id):
        '''delete a student'''
        student = self.find_student(id)
        try:
            if student not in self.student.keys():
                print("This student doesnt exist.")
                raise ValueError
        except Exception:
            print(self.student[id], " is successfully deleted.")
            return self.student.pop([id])

    def search_student(self, search):
        '''search for a student using student id or student email'''
        for student in self.student.items():
            self.stud_id = student[0]
            self.set_email = student[1][1]
        try:
            if self.stud_id == search or self.set_email == search:
                return Student.__str__(search)
               #return self.stud_id, self.stu_name, self.set_email
        except Exception:
            raise ValueError("{} does not exist.".format(search))

    def __str__(self):
        '''Display all college information in a string for users'''
        print("The School of {} offers the following modules. \n".format(self.school_name))
        return {key:value for key,value in self.module.items()}

    def school_menu(self):  # could this be a static method no?

        print("Hello! Welcome to the College Management System. Please choose one of the following:")
        print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        print("1. Add a module.")
        print("2. Delete a module.")
        print("3. View module details.")
        print("4. Add a student.")
        print("5. Delete a student.")
        print("6. View student details.")
        print("7. Search for a student (Student ID or Student email).")
        print("8. Enroll a student in a module.")
        print("9. Un-enroll a student from a module.")
        print("10. Look at School details.")
        print("11. Exit College Management System.")
        print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        option = input("Please enter an option:")
        while option != 11 and option in range(0, 12):
            if option == "1":
                return self.add_module
            elif option == "2":
                code = input("Enter the module code to delete: ")
                return self.delete_module(code)
            elif option == "3":
                module = input("Enter the module you'd like to view: ")
                return Module.__str__(module)
            elif option == "4":
                return self.add_student
            elif option == "5":
                id = input("Enter the student ID to delete: ")
                return self.delete_student(id)
            elif option == "6":
                student = input("Enter the student you'd like to view: ")
                return student.__str__()
            elif option == "7":
                search = input("Enter the student ID or student email you want search: ")
                return search.__str__()
            elif option == "8":
                print("Enrolling Student, please follow the steps.")
                return self.enrollment()
            elif option == "9":
                id = input("Enter the student ID you want to delete: ")
                return self.delete_student(id)
            elif option == "10":
                return self.__str__()
            elif option == "11":
                print("You are now leaving the College Management System, Goodbye!")
            else:
                print("That is an invalid option, please try again.")


# ================================================================================================================#
# Some Instantiations
soc = School("School of Computing")

mod1 = Module("CMPZ163", "System Analysis and Testing", 5)
mod2 = Module("CMPY999", "Information Systems", 5)
mod3 = Module("CMPX001", "OO Software Development", 10)

stu1 = Student("X001200", "Joe Soap")
stu2 = Student("X100001", "Frank Smith")
stu3 = Student("X123120", "Rachel Anderson")

soc.school_menu()
