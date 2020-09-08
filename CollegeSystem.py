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
'''

# ================================================================================================================#
# Modules object used to define each module.
class Modules:

    num_of_modules = 0

    def __init__(self, module_code, module_name, ects_credits, capacity):
        # Initialising Module attributes
        self.module_code = module_code
        self.module_name = module_name
        self.ects_credits = ects_credits
        self.capacity = 0

        Modules.num_of_modules += 1  # count the number of modules

    def get_module(self):
        # Get the module name
        return self.module_name

    def get_code(self):
        # Get the module code
        return self.module_code

    def get_capacity(self):
        # Get the capacity of students
        return self.capacity

    def set_capacity(self):
        # Decrease the capacity when a student enrolls in a module
        try:
            while self.get_capacity() != 0:
                self.capacity = int(self.capacity - 1)
        except ValueError:
            print("{} has reached its maximum capacity.".format(self.module_name))

    def increase_capacity(self):
        # Increase the modules capacity when a student un-enrolls from a module
        self.capacity = int(self.capacity + 1)

    def __str__(self):
        # Display module details in a string for user
        return "Module Code:{0}\nModule Name:{1}\nECTS Credits:{2}\nCapacity:{3}".format(self.module_code, self.module_name,
                                                                               self.ects_credits, self.get_capacity)
    
# ================================================================================================================#
# Student is to define each student and their details, modules list, enroll and un-enroll students
class Students:

    num_of_students = 0

    def __init__(self, stud_id, stu_name, modules=None):
        # Initialising Student attributes
        self.stud_id = stud_id
        self.student_name = stu_name
        self.email = "{}@collegeEmail.com".format(self.stud_id)

        if modules is None:
            self.module_list = []
        else:
            self.module_list = [modules]

        Students.num_of_students += 1  #count the number of students

    # Student menthods
    def get_name(self):
        # Get the students name
        return self.student_name

    def get_id(self):
        # Get the students id
        return self.stud_id

    def module_count(self):
        # Get the length of students module list
        return len(self.module_list)

    def set_module_list(self, module):
        # Add a module to students module list
        try:
            while self.module_count() <= 5:
                self.module_list.append(module)
        except ValueError:
            print("{} has reached their maximum module count".format(self.student_name))

    def __str__(self):
        # Display Student details in a string for users
        print("{0} ({1}), is enrolled in the modules below.\n Email - {2}\n".format(self.student_name, self.stud_id, self.email))
        for i in self.module_list:
            print(i)
        #print([i for i in self.module_list]) This wont work?

# ================================================================================================================#
# Schools object used to define departments that house certain modules and relevant students
class School:

    def __init__(self, school_name):
        # Initialising School and its attributes
        self.school_name = school_name
        self.modules = {}
        self.students = {}
    
    # School methods
    def find_module(self, module_code):
        # Find and return the module code
        try:
            if module_code in self.modules:
                return self.modules.get(module_code)
        except ValueError:
            return "{} cannot be found".format(module_code)

    def find_student(self, stud_id):
        # Find and call the student id
        try:
            if stud_id in self.students:
                return self.students.get(stud_id)
        except ValueError:
            return "{} cannot be found".format(stud_id)

    def enrollment(self):
        # enroll a student in a module
        student_id = input("Enter the student ID: ")
        module_code = input("Enter the module code: ")

        stud_id = self.find_student(student_id)
        modules = self.find_module(module_code)
        try:
            stud_id.module_list.append(modules)
            modules.set_capacity()
            print("{} has successfully enrolled.".format(stud_id))
        except ValueError:
            print("Limit reached.")

    def disenroll(self):
        # disenroll a student from a module, take id and module code
        student_id = input("Enter the student ID: ")
        module_code = input("Enter the module code: ")
        # find student and module
        stud_id = self.find_student(student_id)
        modules = self.find_module(module_code)
        try:
            if modules in stud_id.module_list:
                stud_id.module_list.remove(modules)
                modules.increase_capacity()
                print("{0} has successfully un-enrolled from {1}.".format(stud_id, modules))
        except ValueError:
            print("{0} does not appear to be in enrolled in {1}.").format(stud_id, module_code)

    def add_module(self):
        # create and add a module to modules, additional error checks
        module_code = input("Enter Module code: ")
        try:
            while len(module_code) == 6:
                break
        except:
            print("Module Code should be 6 characters.")

        module_name = input("Enter Module name: ")
        try:
            while len(module_name) > 2 and len(module_name) < 30:
                break
        except:
            print("Module name need to be between 2 and 30 characters.")

        ects_credits = 0
        capacity = 0
        while True:
            try:
                ects_input_str = input("Enter Modules ECTS Credits: ")
                ects_credits = int(ects_input_str)
                break
            except ValueError:
                print("Invalid input for ECTS credits, must be a number")

        while True:
            try:
                capacity_str = input("Enter the modules current capacity: ")
                capacity = int(capacity_str)
                break
            except ValueError:
                print("Invalid input for ECTS credits, must be a number")
        new_module = Modules(module_code, module_name, ects_credits, capacity)
        self.modules[module_code] = new_module

    def delete_module(self, code):
        # delete a module
        mod = self.find_module(code)
        try:
            # find module
            if mod not in self.modules.items():  
                print("This module doesnt exist.")
                raise ValueError
        except:
            return self.modules.pop(code)

    def add_student(self):
        # create and add a student with error checks
        student_name = input("Enter Student name: ")
        name_length = len(student_name)
        try:
            while name_length > 1 and name_length < 31:
                break
        except ValueError:
            print("Student name must be between 1 and 30 characters.")
        stud_id = input("Enter Student ID: ")
        try:
            while len(stud_id) == 6:
                break
        except ValueError:
            print("Student ID needs to be 6 characters.")

        try:
            if stud_id in self.students:
                print("{} already exits.\n".format(stud_id))
        except ValueError:
            print("Invalid input.")

        new_student = Students(stud_id, student_name)
        self.students[stud_id] = new_student

    def delete_student(self, student_id):
        # delete a student
        student = self.find_student(student_id)
        try:
            if student in self.students.items():
                return self.students.pop(id)
        except ValueError:
            print("{} doesnt exist in the system.".format(student))

    def search_student(self, search):
        # search for a student using student id or student email
        for kvp in self.students.items():
            try:
                if search == kvp.stud_id or search == kvp.email:
                    print(self.students[stud_id])
                elif search == kvp.student_name:
                    print("Incorrect search type", TypeError)
            except ValueError:
                print("{} does not exist in the system.".format(search))

    def print_module_details(self, module_code):
        self.find_module(module_code)
        print(self.modules[module_code])

    def print_student_details(self):
        # Print searched student
        student_id = input("Enter the students ID to view their details: ")
        self.find_student(student_id)
        print(self.students[student_id])
        # print(student_details)
        # print(student_details.module_list)

    def print_all_students(self):
        # Print all student details
        print("The following students have registered in the {}. \n".format(self.school_name))
        try:
            for stud in self.students.items():
                print(self.students)
        except ValueError:
            print("No students have been registered, please add some students.")

    def __str__(self):
        '''Display all modules in the college'''
        print("The {} offers the following modules. \n".format(self.school_name))
        try:
            for mod in self.modules.items():
                print(self.modules)
        except ValueError:
            print("No Modules have been created, please add some modules.")

    def school_menu(self):
        #School menu for user interaction plus system operations
        
        print("Hello! Welcome to the College Management System. Please choose one of the following options:")
        while True:
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
            print("10. View all students in the school.")
            print("11. View all modules in the school.")
            print("12. Exit College Management System.")
            print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
            option = input("Please enter an option:")
            try:
                input_val = int(option)
            except ValueError:
                print("\n'{}' is an invalid option, your input should be between 1-12.".format(option))
                continue

            if input_val == 1:
                self.add_module()
                print("Module added successfully.")

            elif input_val == 2:
                code = input("Enter the module code to delete: ")
                self.delete_module(module_code)
                print("Module deleted successfully.")

            elif input_val == 3:
                code = input("Enter the module code to view the module: ")
                self.print_module_details(module_code)
                input_val = input("\nPress any key to continue.")

            elif input_val == 4:
                self.add_student()
                print("Student added successfully.")

            elif input_val == 5:
                student_id = input("Enter the student ID to delete: ")
                self.delete_student(student_id)
                print("Student deleted successfully.")

            elif input_val == 6:
                self.print_student_details()
                input_val = input("\nPress any key to continue.")

            elif input_val == 7:
                search = input("Enter the student ID or student email you want search: ")
                self.search_student(search)
                input_val = input("\nPress any key to continue.")

            elif input_val == 8:
                print("Enrolling Student, please follow the steps.")
                self.enrollment()

            elif input_val == 9:
                print("Un-enrolling Student, please follow the steps.")
                self.disenroll()

            elif input_val == 10:
                self.print_all_students()
                input_val = input("\nPress any key to continue.")

            elif input_val == 11:
                School.__str__(self)
                input_val = input("\nPress any key to continue.")

            elif input_val == 12:
                print("\nYou are now leaving the College Management System, have a nice day and stay safe!")
                break
            else:
                if input_val not in range(13):
                    print("\n'{}' is an invalid option, your input should be between 1-11.".format(input_val))

# ================================================================================================================#
# Some Instantiations
soc = School("School of Computing")

# mod1 = Modules("CMPZ163", "System Analysis and Testing", 5, 0)
# mod2 = Modules("CMPY999", "Information Systems", 5, 0)
# mod3 = Modules("CMPX001", "OO Software Development", 10, 0)
#
# stu1 = Students("X001200", "Joe Higgins", )
# stu2 = Students("X100001", "Frank Smith", )
# stu3 = Students("X123120", "Rachel Anderson", )

soc.modules = {}
soc.students = {}

soc.school_menu()
