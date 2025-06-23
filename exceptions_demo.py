# first_num = int(input('Enter First number: '))
# second_num = int(input('Enter Second number: '))
# print(f'first number divided by second number is {first_num / second_num}')

class Negativenumbererror(Exception):
    def __init__(self, message='The number is a negative number'):
        super().__init__(message)


def check_positivenumber(number):
    if number < 0:
        raise Negativenumbererror()


try:
    check_positivenumber(-2)
except Negativenumbererror as  ex:
    print(ex)