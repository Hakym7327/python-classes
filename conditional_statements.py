# If statement

# if bool_expr:
    # body 


# 2 is greater than 5
# num1 = 50
# num2 = 70

# if num1 == num1:
#     print("Num 1 is actually equal to 3")



# WRite a program that takes a number and tells whether the number is exactly 15
# number = int(input('ENter a number: '))

# if number == 15:
#     print(number,'is equal to 15')
# else:
#     print(number, 'is NOT equal to 15')


# Write a program that takes a user's name and age and tells if the user is eligible to vote
# Tobi, sorry, you're not eligible to vote.
# Congrats, Tobi, you are eligible to vote

# name = input('Enter your name: ')
# age = int(input('Provide your age: '))
# is_student = input('Are you a student? yes/no: ')

# if (age < 18 or age > 70) and is_student == 'yes':
#     print(name, 'Sorry... you are NOT eligible')
# elif (age < 18 or age > 70) and is_student == 'no':
#     print(name, 'Sorry, although you are not a student, your age won\'t allow you to vote')
# elif (18 <= age <= 70 ) and is_student == 'yes':
#     print(name, 'Sorry, you still can\'t vote because you are still a student')

# # 18 - 70, student
# else:
#     print( f"Congrats, {name}, you are eligible to vote")



# Variable called 
has_umbrella = True
has_raincoat = True

# You are WELL PROTECTED from the rain if you have both umbrella and raincoat
# You are PROTECTED from the rain if you have either umbrella or raincoat
# You are NOT PROTECTED from the rain if they have neither

# # Mr. Hakeem.
# if has_umbrella and has_raincoat:
#     print("You are well protected from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected from the rain")
# else:
#     print('You are NOT protected from the rain.')


# # Mr. Niko
# has_umbrella = True
# has_raincoat = True
# if has_umbrella and has_raincoat:
#     print("You are WELL protected from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected from the rain")
# else:
#     print(' You are not PROTECTED from the rain')


# name = input('Enter your name: ').strip()
# if name:
#     print('Good morning,', name)
# else:
#     print('You do NOT have a name')




# name = input('Enter your name: ')
# if name.isspace():
#     print('You do NOT have a name')
# else:
#     print('Good morning,', name)


# # Using falsy and truthy values in if statements.
# # pass
# # ternary operator
# # nested ifs


# "", 0, 0.0, None, [], {}, set()'

# b = int(input('ENter something here: '))

# if b == 8 and "": 
#     print("")



# students = input('Enter your student names separated by comma: ')

# if not students:
#     print('Enter at least one student')
# students =  ['tobi', 'john', 'james']

# students = students.split(',')

# if students:
#     print('There are students here.')
# else:
#     print('There are no students here.')


# if len(students) == 0:


# mood = ""

# # if mood variable is empty
# if not mood:
#     print('Mood is empty')
# else:
#     print('Mood is not empty')




# mood = ""

# # if mood variable is empty
# if not mood:
#     # this should do something
#     pass
# else:
#     pass



# Ternary operator
# gender = "males"
# pronoun = "he" if gender == 'male' else "she"

# print("he" if gender == 'male' else "she")

# print(pronoun)

# if gender == 'male':
#     pronoun == 'he'
# else:
#     pronoun == 'she'

# variable = first_value if statement... else second_value




# age = 21
# gender = 'dog'

# if gender == 'male':
#     if age < 18:
#         print('You are male but cannot vote')
#     else:
#         print('You are male and you can vote')
# elif gender == 'female':
#     print('Women are not allowed to vote')
# else:
#     print('Invalid gender')




# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off". If the option is invalid, say it's invalid.


options = ["manual", "automatic", "off"]


