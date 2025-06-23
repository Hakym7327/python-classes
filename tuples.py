# names_tuple = ("Tobi", "Tade", "James", "Tobi")

# # print(names_tuple)

# # We have "10" number of names

# print(f"We have \"{{len(names_tuple)}}\" number of names")

# print('Type of names_tuple: ', type(names_tuple))


# name = ["Tobi", "Bode"]
# # print(type(name))
# # print(dir(name))
# name = tuple(name)
# print(type(name))

# # print(dir(name))
# name.append("Tobi")
# # int, str, list, tuple



# names_tuple = ("Tobi", "Tade", "James", "Tobi")

# names_tuple = list(names_tuple)
# names_tuple.remove('James')
# names_tuple = tuple(names_tuple)
# print(names_tuple)


# other_names = ("JOhnny", "Kane", "Hillary")

# del other_names

# all_names = names_tuple + other_names

# print('All our names: ', all_names)


# # del keyword

names = ("Ade", "Ball", "Cup", 33 > 348, False)

# name, item, *_ = names
name, item, *_, bool2 = names
print(bool2)
# print(others)
# print("""
      
#       """)


_, item, _, bool1, bool2 = names

print(_)
print(item)

# unpacking multiple values
# unpacking nested values
# swapping values

# Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])

# name, age_position, departments = record

# age, position = age_position
# dept1, dept2 = departments



# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, position), (dept1, dept2) = record

# print('Age: ',age)
# print("Department 1: ", dept1)


# record = ("Jane", (32, ("MD", "Manager")), ["HR", "Finance"])
# name, (age, (pos1, pos2)), (dept1, dept2) = record

# print("Position: ", pos2)



# num1 = 65
# num2 = 88

# num3 = num1
# print(num1, num2)

# num1 = num2
# num2 = num3

# print(num1, num2)




num1 = 65
num2 = 88
print(num1, num2)

num1, num2 = num2, num1
print(num1, num2)




