# Documentation string
# The multiline string must be placed at the top of the function.

# def add(a, b):
    
#     '''
#     My function here just returns the addition of a and b
#     Returns:
#     int, float: The sum of the two numbers.
#     '''
#     return a + b




# def power(base, exponent): # 10,     3
#     # 10 * (10, 2) * 10 * 1
#     if exponent == 0:  # Base case
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call






# Object Oriented Programming

# students = [
#     {'id': 1, 'name': "Tobi", "salary": 183883},
#     {'id': 2, 'name': "Niko", "salary": 594949}
# ]




# def add_to_salary(id, salary):
    
#     selected_student = None
    
#     for student in students:
#         if student['id'] == id:
#             selected_student = student
#             break
    
#     selected_student['salary'] += salary     

# students = [
#     {'id': 1, 'name': "Tobi", "salary": 183883},
#     {'id': 2, 'name': "Niko", "salary": 594949}
# ]



# def add_to_salary(id, salary):
    
#     for student in students:
#         if student['id'] == id:
#             student['salary'] += salary
#             break
#     print(salary,'added to student with id "', id, '"')
            
    

# print(students)

# add_to_salary(1, 20000)

# print(students)




# add_to_salary()



# Classes       
# 


# class Student:
    
#     is_nigerian = True

    
#     def subtract_salary(id, salary):
    
#         for student in students:
#             if student['id'] == id:
#                 student['salary'] -= salary
#                 break
#         print(salary,'added to student with id "', id, '"')
    
            

# std1 = Student("Tobi Dada", "20000") # object
# std2 = Student("Niko", "80000")
# std3 = Student()
# std4 = Student()


# print(std1.is_nigerian)
# # It's a blueprint for creating objects




class Employee:
    
    def employee_salary(self):
        return self.salary
    
    def emp_name(self):
        return self.name
    

    def __init__(self, id, name, salary): # Constructor
        self.id  = id
        self.name = name
        self.salary = salary


# emp1 = Employee(4, "Rice Greezeman", 185000)
# emp2 = Employee(5, "Hakym", 6000)

# print('Employee 2: ', emp2.name)


# It's just a design pattern / paradigm


# A constructor is a method that automatically gets executed everytime you create an object



# students = [
#     {'id':1, 'name': "Tobi Dada", "matric": 'E047317', "course": "CSC"},
#     {'id':2, 'name': "Hakym", "matric": "E048823", "course": "Mathematics"},
#     {'id':3, "name": "Niko", "matric": "E047883", "course": "Physics"}    
# ]


# def get_matric(id):
#     for student in students:
#         if student["id"] == id:
#             return student['matric']


# def get_full_details(id):
#     for student in students:
#         if student['id'] == id:
#             return student

# print(get_full_details(3))

#

# object
 # you caling teh class name

# emp1 = Employee(1, "Tobi", "$20000")
# emp2 = Employee(2, "James", "$1800")
# emp3 = Employee(6, "Johnny", "$2000")
# print(emp2.salary)
# print('Employee name: ', emp3.name)




# class Student:
#     # id = 1   # Attributes or fields
#     # name = "Toi Daa"
#     # course = "Computer Science"
#     # matric = "E0488834"
    
#     def get_name_and_course(self):
#         return f'{self.name} {self.course}'  # interpolation
    
#     def __init__(self, id, name, course, matric ):
#         self.id = id
#         self.name = name
#         self.course= course
#         self.matric = matric
        
#     def get_registered_courses(self):
#         return self.course
        
        


# std1 = Student(188, "TINUBU", "Computer Science", "E048883")
# std2 = Student(102, "LAPTOP MAN", "Physics", "293993")
# # std2 = Student()
# print(std1.get_name_and_course())

# print(std2.get_name_and_course())





# emp2 = Employee()
# emp3 = Employee()
# emp4 = Employee()

    



# question_bank = [
#     {'question': "Why is the sky so blue?", "answer": "c", "options": "a. Moon\nb. I dont know\nc. Random"},
#     {'question': "What is 2 + 2?", "answer": "b", "options": "a. 5\nb. 4\nc.8"},
    
# ]

# score  =0

# for question in question_bank:
#     print(question['question'])
#     print('Choose an option\n', question['options'])
#     user_answer = input()
    
#     if user_answer == question['answer']:
#         score += 5

# print('Total score: ', score)











class Person:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    




class Student(Person):
    
    def get_name_and_course(self):
        return f'{self.name} {self.course}'  # interpolation
    
    def __init__(self, course, matric ):
        self.course= course
        self.matric = matric
        
    def get_registered_courses(self):
        return self.course
        

std1 = Student(188, "TINUBU", "Computer Science", "E048883")
std2 = Student(102, "LAPTOP MAN", "Physics", "293993")
# std2 = Student()
print(std1.get_name_and_course())

print(std2.get_name_and_course())



