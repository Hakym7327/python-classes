
def sum_all(*args):
    return sum(args)


print(sum_all())


# arbitrary keyword arguments


def sum_all(**kwargs):
    print(kwargs)


sum_all(a=42, b=88, d="Tobi")


def sum_all(*args, **kwargs):
    print(kwargs)
    print(args)


sum_all([], 32, 488, a=42, b=88, d="Tobi")



def sum_all(num1, num2, *args, **kwargs):
    print(num1)
    print(num2)
    print(kwargs)
    print(args)


sum_all([], 32, 488, a=42, b=88, d="Tobi")





def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}", end=', ')
# pass any number of keyword arguments
greet(name="John", greeting="Hello", state = "Oyo")







# Calculator project
#Performs addition of two numbers.

def addition(num1, num2): 
    return num1 + num2

# Performs subtraction of two numbers.
def subtraction(num1, num2): 
    return num1 - num2


# Performs multiplication of two numbers.
def multiplication(num1, num2): 
    return num1 * num2


# Perform the division of two numbers

def division(num1, num2):
    if  num2 == 0:
        return "Error... Second number must not be zero"
    
    return f"Division of {num1} and {num2} = {num1/num2}"

while True:
    print("""
    Welcome to the Simple Calculator
    
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit""")

    option = int(input('Choose an option: '))

    if option in [1, 2, 3, 4]:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))

        if option == 1:
            print(f"Sum of {a} and {b} = {addition(a, b)}")
        elif option == 2:
            print(f"Subtraction of {a} and {b} = {subtraction(a, b)}")
        elif option == 4:
            print(division(a, b))


    elif option == 5:
        print('Exiting the program...')
        break
    else:
        print('Invalid option')
# Very short simple way to build a calculator in python using eval function