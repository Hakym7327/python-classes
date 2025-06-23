# # # # # # # # # car_name = 'Volvo'
# # # # # # # # # x = 50
# # # # # # # # # #d
# # # # # # # # # #d

# # # # # # # # # name = 'Hakym'
# # # # # # # # # print(type(name))
# # # # # # # # # age = 74
# # # # # # # # # print(type(age))
# # # # # # # # # height = 1.7
# # # # # # # # # print(type(height))
# # # # # # # # # is_student = True
# # # # # # # # # print(type(is_student))

# # # # # # # # # first_name = 'John'
# # # # # # # # # last_name = 'Smith'
# # # # # # # # # print(first_name + ' ' + last_name)

# # # # # # # # # word = "python"
# # # # # # # # # print(word[0])

# # # # # # # # # string1 = 'Data'
# # # # # # # # # string2 = 'Science'
# # # # # # # # # print(string1 + string2)

# # # # # # # # # phase = 'Welcome'
# # # # # # # # # print(phase[-1])


# # # # # # # # # New Assignment 10/4/25

# # # # # # # # # 35.Given the string course_name = "Introduction to Python", use slicing to print:
# # # # # # # # # The word "Introduction".
# # # # # # # # # The word "Python".
# # # # # # # # course_name = "Introduction to Python"
# # # # # # # # print(course_name [0 : 12], course_name[-6 :])

# # # # # # # # # 36.Given the string quote = "To be or not to be, that is the question.", use slicing to print:
# # # # # # # # # The substring "To be or not to be".
# # # # # # # # # The substring "that is the question".
# # # # # # # # quote = "To be or not to be, that is the question."
# # # # # # # # print(quote [0 : 18])
# # # # # # # # print(quote [20 : 40])

# # # # # # # # # 37.Given the string phrase = "A journey of a thousand miles begins with a single step", use 
# # # # # # # # # slicing to print:
# # # # # # # # # The last 5 characters.
# # # # # # # # # All characters except the last 7.
# # # # # # # # phrase = "A journey of a thousand miles begins with a single step"
# # # # # # # # print(phrase[-4 : len(phrase)])
# # # # # # # # print(phrase[0 : -7])

# # # # # # # # # 38.Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", use slicing to print:
# # # # # # # # # Every second letter (A, C, E, ...).
# # # # # # # # # Every third letter starting from the first letter (A, D, G, ...).
# # # # # # # # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # # # # # # # print(alphabet[0 : len(alphabet) : 2])
# # # # # # # # print(alphabet[0 : len(alphabet) : 3])

# # # # # # # # # 39.Given the string word = "tenet", use slicing to:
# # # # # # # # # Reverse the string and print the result.
# # # # # # # # word = "tenet"  #palindrome word which means reverse and original are the same.
# # # # # # # # print(word[::-1])

# # # # # # # # # 40.Given the string sentence = "Learning Python is fun and rewarding!", use slicing to print:
# # # # # # # # # Characters from index 9 to 19. (Python is f)
# # # # # # # # # Every second character from index 0 to 10. (Lann y)
# # # # # # # # # Every third character from the beginning to the end. (LrnPh  nnrai!)
# # # # # # # # sentence = "Learning Python is fun and rewarding!"
# # # # # # # # print(sentence[9 : 20])
# # # # # # # # print(sentence[0 : 11 :2])
# # # # # # # # print(sentence[0 : len(sentence) : 3])

# # # # # # # # # 41.Given the string programming_language = "JavaScript", use slicing to:
# # # # # # # # # Print the first character.
# # # # # # # # # Print the last character.
# # # # # # # # programming_language = "JavaScript"
# # # # # # # # print(programming_language[0])
# # # # # # # # print(programming_language[-1])

# # # # # # # # # 42.	Given the string data = "DataScience", use slicing to:
# # # # # # # # # Print the substring "Science".
# # # # # # # # data = "DataScience"
# # # # # # # # print(data[4 : len(data)])

# # # # # # # # # 43.Given the string greeting = "Good Morning!", use slicing to:
# # # # # # # # # Print every second character.
# # # # # # # # greeting = "Good Morning!"
# # # # # # # # print(greeting[:: 2])

# # # # # # # # # 44.Given the string name = "Alexander", use slicing to:
# # # # # # # # # Print the first three characters concatenated with the last three characters.
# # # # # # # # name = "Alexander"
# # # # # # # # print(name[: 3] + name[-3 :])

# # # # # # # # 14/4/25

# # # # # # # # 17.	Convert a string “James John Kennedy” called “names” to a list using the string 
# # # # # # # # .split() method. Store the result in a list called “names_list”
# # # # # # # names = 'James John Kennedy' 
# # # # # # # names_list = names.split()
# # # # # # # print(names_list)

# # # # # # # # 18.You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# # # # # # # # 'Chicago']. Convert this list into a single string where each city is separated by a 
# # # # # # # # semicolon and a space. Store the result in a string called cities_string.
# # # # # # # cities_list = ['New York', 'Los Angeles','Chicago']
# # # # # # # cities_string = '; ' .join(cities_list)
# # # # # # # print(cities_string)

# # # # # # # # 19.Create a string variable sentence with the value "the quick brown fox jumps over the 
# # # # # # # # lazy dog". Capitalize the first letter of the string and 
# # # # # # # # print the result.
# # # # # # # sentence = "the quick brown fox jumps over the lazy dog"
# # # # # # # x = sentence .capitalize()
# # # # # # # print(x)

# # # # # # # # 20.Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# # # # # # # # the first letter of each word and print the result.
# # # # # # # book_title =  "to kill a mockingbird"
# # # # # # # y = book_title .title()
# # # # # # # print(y)

# # # # # # # # 21.Create a string variable text with the value "hello world". Count the number of 
# # # # # # # # occurrences of the letter 'o' and print the result.
# # # # # # # text =  "hello world"
# # # # # # # print(text .count('o'))

# # # # # # # # 22.Create a string variable filename with the value "document.txt". Check if the string 
# # # # # # # # starts with "doc" and print the result.
# # # # # # # filename =  "document.txt"
# # # # # # # print(filename .startswith('doc'))

# # # # # # # # 23.Create a string variable url with the value "https://www.example.com". Check if the 
# # # # # # # # string ends with ".com" and print the result.
# # # # # # # url =  "https://www.example.com"
# # # # # # # print(url .endswith('.com'))

# # # # # # # # 24.Create a string variable phrase with the value "find the needle in the haystack". Find 
# # # # # # # # the position of the word "needle" and print the result.
# # # # # # # phrase = "find the needle in the haystack"
# # # # # # # print(phrase .find('needle')) 

# # # # # # # # 25.Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# # # # # # # # format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# # # # # # # # Result. Bonus point if you can do it with the f-string and concatenation methods also.
# # # # # # # template =  "Hello, {} Welcome to {}."
# # # # # # # print(template  .format('Alice','Wonderland'))

# # # # # # # # 26.Create a string variable `quote` with the value "To be or not to be". Find the position 
# # # # # # # # of the word "not" and print the result.
# # # # # # # quote = "To be or not to be"
# # # # # # # print(quote .find('not'))

# # # # # # # # 27.Create a string variable word with the value "hello". Check if all characters in the 
# # # # # # # # string are lowercase and print the result.
# # # # # # # word = "hello"
# # # # # # # print(word .islower())

# # # # # # # # 28.Create a string variable shout with the value "HELLO". Check if all characters in the 
# # # # # # # # string are uppercase and print the result.
# # # # # # # value = 'HELLO'
# # # # # # # print(value .isupper())

# # # # # # # # 29.Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# # # # # # # # lowercase and print the result.
# # # # # # # mixed_case =  "PyThOn"
# # # # # # # print(mixed_case .lower())

# # # # # # # # 30.Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# # # # # # # # uppercase and print the result.
# # # # # # # mixed_case =  "PyThOn"
# # # # # # # print(mixed_case .upper())

# # # # # # # # 31.Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# # # # # # # # print the result.
# # # # # # # padded_text = " hello "
# # # # # # # print(padded_text .lstrip())

# # # # # # # # 32.Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# # # # # # # # print the result.
# # # # # # # padded_text = " hello "
# # # # # # # print(padded_text .rstrip())

# # # # # # # # 33.Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# # # # # # # # print the result.
# # # # # # # padded_text = " hello "
# # # # # # # print(padded_text .strip())

# # # # # # # # 34.Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# # # # # # # # and print the result.
# # # # # # # greeting = "Hello, World!"
# # # # # # # print(greeting .replace('World','Alice'))



# # # # # # # 16/4/2025
# # # # # # # 1 Write a program that asks the user for their name and then greets them with their 
# # # # # # # name: Print a greeting message that includes the user's name in the format "Hello, {name}!".

# # # # # # # name = input('Enter your name: ')
# # # # # # # print(f'Hello, {name}')

# # # # # # # 2 Ask the user for their birth year and calculate their age. Print the user's age in the 
# # # # # # # format “You are {age} years old.”.

# # # # # # # from datetime import datetime
# # # # # # # birth_year = input('What is your birth year: ')
# # # # # # # current_year = datetime.today().year
# # # # # # # age = current_year - int(birth_year)
# # # # # # # print(f'You are {age} years old.')

# # # # # # # 3 Ask the user for their favourite color. Print a statement that includes the color in the format 
# # # # # # # “Your favorite color is {favourite_color}.”.

# # # # # # # fav_color = input('Enter your favorite color: ')
# # # # # # # print(f'Your favorite color is {fav_color}')

# # # # # # # 4 Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or 
# # # # # # # sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# # # # # # # Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome`
# # # # # # # is either `True` or `False`and its used to check if strings or lists are the same in thr system's memory while
# # # # # # # == is used to acertain if variables are the same.

# # # # # # # word = input('Enter a text or phrase to check if its a palindrome: ')
# # # # # # # word = word.replace(' ', '')
# # # # # # # word = word.lower()
# # # # # # # is_palindrome = word == word[::-1]
# # # # # # # print(f'It is {is_palindrome} that {word} is a palindrome.')

# # # # # # # 5 Create a program that asks the user to input a password and checks if it meets certain criteria 
# # # # # # # (at least 8 characters and not more than 30 characters).
# # # # # # # Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. 
# # # # # # # `is_valid` is either `True` or `False`.
# # # # # # # Bonus point if you can hide the password input from displaying on the screen as clear text.

# # # # # # password = input('Enter your Password: ')
# # # # # # is_valid = password >= len(password)
# # # # # # print(password)

# # # # # # # 6 Write a program that asks the user for their weight (in kilograms) and height (in meters) and 
# # # # # # # calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2).
# # # # # # #  Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.

# # # # # # # weight = input('Input your weight in meters: ')
# # # # # # # height = input('Input your height in meters: ')
# # # # # # # BMI = int(weight) / (int(height) ** 2)
# # # # # # # BMI = '{0:.2f}'.format(BMI)
# # # # # # # print(f'Your BMI is {BMI}')

# # # # # # # Game 3

# # # # # # term_of_endearment = input('Enter Term of Endearment: ')
# # # # # # first_name = input('Enter Your Firstname: ')
# # # # # # firstname_lastname = input('Enter Your Firstname and Lastname: ')
# # # # # # place = input('Enter a place: ')
# # # # # # day_of_the_week = input('Enter a day of the week: ')
# # # # # # adjective= input('Enter an adjective: ')
# # # # # # color = input('Enter a color: ')
# # # # # # item_of_clothing = input('Enter an item of clothing: ')
# # # # # # number =  input('Enter a number: ')
# # # # # # verb = input('Enter a verb: ')
# # # # # # verb_2 = input('Enter a verb: ')
# # # # # # verb_3 = input('Enter a verb: ')
# # # # # # verb_4 = input('Enter a verb: ')

# # # # # # story = f"""Hey, {term_of_endearment}. What's up? You know,
# # # # # # {first_name}. {firstname_lastname}.From the {place}.
# # # # # # Two {day_of_the_week}s ago. I was the {adjective} guy 
# # # # # # in the {color} parachute {item_of_clothing}. I paid the bus boy
# # # # # # {number} dollars to {verb} me your information. I was 
# # # # # # wondering if maybe you'd like to {verb_2} out with me. 
# # # # # # Please dont call the {verb_3} department. Alright, I will {verb_4}.
# # # # # #  So, that's a no, right?"""

# # # # # # print(story)

# # # # # # 17/4/2025

# # # # # # Assignnment 1

# # # # # # # 1 Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
# # # # # # fruits = ["apple", "banana", "orange"]
# # # # # # print(fruits[0])

# # # # # # # 2 Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
# # # # # # items = ["red", "green", "blue"]
# # # # # # print(fruits[-1])

# # # # # # # 3 Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
# # # # # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # # # print(numbers[3:8])

# # # # # # # 4 Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
# # # # # # alphabets = ["a", "b", "c", "z"]
# # # # # # print(alphabets[-3:])

# # # # # # # 5 Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
# # # # # # alphabets = [ 20, 30, 40]
# # # # # # alphabets[1] = 35
# # # # # # print(alphabets)

# # # # # # # 6 Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
# # # # # # grades = ["A", "B", "C", "D"]
# # # # # # grades[1:4] = ['X']
# # # # # # print(grades)

# # # # # # # 7 Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
# # # # # # cities = ["New York", "London", "Paris"]
# # # # # # cities.insert(0, 'Tokyo')
# # # # # # print(cities)

# # # # # # # 8 Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
# # # # # # fruits = ["apple", "banana", "cherry"]
# # # # # # print(len(fruits))

# # # # # # # 9 Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
# # # # # # prices = [10.5, 20.0, 15.75]
# # # # # # print(type(fruits))

# # # # # # # 10 Create a list called mixed with items 10, "apple", True. Print the list.
# # # # # # mixed = [10, "apple", True]
# # # # # # print(mixed)

# # # # # # # 11 Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
# # # # # # tuple_data = ("a", "b", "c")
# # # # # # print(list(tuple_data))

# # # # # # # 12 Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
# # # # # # books = ["Python", "Java"]
# # # # # # books.append("JavaScript")
# # # # # # print(books)

# # # # # # # 13 Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
# # # # # # names = ["Alice", "Bob", "Eve"]
# # # # # # names.insert(1, "Charlie" )
# # # # # # print(names)

# # # # # # # 14 Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
# # # # # # list1 = [1, 2, 3 ]
# # # # # # list2 = [4, 5, 6 ]
# # # # # # list1.extend(list2)
# # # # # # print(list1)

# # # # # # # 15 Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
# # # # # # students = ["Alice", "Bob"]
# # # # # # tuple = ("Charlie", "David")
# # # # # # students.extend(tuple)
# # # # # # print(students)

# # # # # # # 16 Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
# # # # # # colors = ["red", "green", "blue"]
# # # # # # colors.remove("green" )
# # # # # # print(colors)

# # # # # # # 17 Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
# # # # # # numbers = [10, 20, 30, 40]
# # # # # # del numbers[2]
# # # # # # print(numbers)

# # # # # # # 18 Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
# # # # # # fruits = ["apple", "banana", "cherry"]
# # # # # # fruits.clear()
# # # # # # print(fruits)

# # # # # # # 19 Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
# # # # # # names = ["Zoe", "Alice", "Bob"]
# # # # # # names.sort()
# # # # # # print(names)

# # # # # # # 20 Create a list called ages with items 25, 35, 20. Sort the list in descending order.
# # # # # # ages = [25, 35, 20]
# # # # # # ages.sort(reverse=True)
# # # # # # print(ages)

# # # # # # # 21 Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# # # # # # #    "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
# # # # # # words = ["Apple", "banana", "Orange"]
# # # # # # # words1 = [word.capitalize() for word in words]
# # # # # # words.sort(key=str.lower)
# # # # # # print(words)

# # # # # # # 22 Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
# # # # # # numbers = [1, 2, 3, 4]
# # # # # # numbers.reverse()
# # # # # # print(numbers)

# # # # # # # 23 Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
# # # # # # # 	 slicing.
# # # # # # letters = ["a", "b", "c", "d"]
# # # # # # print(letters[::-1])

# # # # # # # 24 Create a list called original with items "one", "two", "three". Create a copy of the list.
# # # # # # original = ["one", "two", "three"]
# # # # # # original2 = original.copy()
# # # # # # print(original2)

# # # # # # # 25 Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
# # # # # # # 	 list2 together.
# # # # # # list1 = ["a", "b" ]
# # # # # # list2 = ["c", "d" ]
# # # # # # list3 = list1 + list2
# # # # # # print(list3)

# # # # # # # 26 Access and print the second subject of the first person in the list.
# # # # # # data = [
# # # # # #     ["Alice", 25, ["Math", "Physics"]],
# # # # # #     ["Bob", 30, ["Chemistry", "Biology"]],
# # # # # #     ["Charlie", 35, ["History", "Geography"]]
# # # # # # ]
# # # # # # print(data[0][2][1])

# # # # # # # 27 Access and print the first value in the list of numbers associated with "San Francisco".
# # # # # # records = [
# # # # # #     ["New York", [10, 20, 30]],
# # # # # #     ["San Francisco", [40, 50, 60]],
# # # # # #     ["Austin", [70, 80, 90]]
# # # # # # ]
# # # # # # print(records[1][1][0])


# # # # # # # 22/4/25
# # # # # # # 1.Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# # # # # # # length, width, and height, and print each variable.
# # # # # # dimensions = (10, 20, 30)
# # # # # # length, width, height = dimensions
# # # # # # print(length)
# # # # # # print(width)
# # # # # # print(height)

# # # # # # # 2.Given the tuple coordinates:
# # # # # # # coordinates = (1.5, 2.5, 3.5)
# # # # # # # Unpack the tuple into variables x, y, and z, and print the value of y.
# # # # # # coordinates = (1.5, 2.5, 3.5)
# # # # # # x, y, z = coordinates
# # # # # # print(y)

# # # # # # # 3.Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession.
# # # # # # person = ("John", 25, "Engineer") 
# # # # # # name, age, profession = person
# # # # # # print(profession)

# # # # # # # 4.Given the nested tuple data:
# # # # # # # Unpack the first element of data into variables student1 and student2, and print student2.
# # # # # # data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# # # # # # (student1, student2), *_ = data
# # # # # # print(student2)


# # # # # # # 5.Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables.
# # # # # # colors = ("red", "green", "blue", "yellow")
# # # # # # colors1, colors2, *_ = colors
# # # # # # print(colors1)
# # # # # # print(colors2)

# # # # # # # 6.Given the tuple record:
# # # # # # # record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# # # # # # # # Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
# # # # # # # name, (age, position), (dept1, dept2) = record
# # # # # # # print(age)
# # # # # # # print(dept1)


# # # # # # # # 7.Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.
# # # # # # # triplet = ("one", "two", "three")
# # # # # # # triplet1, triplet2, triplet3 = triplet
# # # # # # # print(triplet2)


# # # # # # # # 8.Given the tuple info:
# # # # # # # info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# # # # # # # # Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.
# # # # # # # product_ID, (category, price), (manufacture_day, manufacture_month, manufacture_year) = info
# # # # # # # print(category)
# # # # # # # print(manufacture_year)


# # # # # # # # 9.Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack the nested tuples into individual variables and print the second value of the third tuple.
# # # # # # # nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
# # # # # # # (alphabet1, alphabet2), (alphabet3, alphabet4), (alphabet5, alphabet6) = nested_tuple
# # # # # # # print(alphabet6)

# # # # # # # # 10.Given the tuple inventory:
# # # # # # # inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# # # # # # # # Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
# # # # # # # (fruit1, quantity1), (fruit2, quantity2), (fruit3, quantity3) = inventory
# # # # # # # print(f'The quantity of {fruit2} is {quantity2}')


# # # # # # # 23/4/25
# # # # # # # Nested Dictionaries

# # # # # # # 1.Access and print the name of the teacher of "class2".
# # # # # # school = {
# # # # # #     "class1": {
# # # # # #         "students": ["Alice", "Bob"],
# # # # # #         "teacher": "Mr. Smith"
# # # # # #     },
# # # # # #     "class2": {
# # # # # #         "students": ["Charlie", "David"],
# # # # # #         "teacher": "Ms. Johnson"
# # # # # #     }
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'name of teacher of class2: {school ["class2"]["teacher"]}')

# # # # # # # 2.Access and print the second employee in the "Engineering" department.
# # # # # # company = {
# # # # # #     "HR": ["Alice", "Bob"],
# # # # # #     "Engineering": ["Charlie", "David"]
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'The second employee of the "Engineering department: {company["Engineering"][1]}')

# # # # # # # 3.Access and print the name of the second assistant.
# # # # # # university = {
# # # # # #     "faculty": {
# # # # # #         "professors": ["Dr. Smith", "Dr. Brown"],
# # # # # #         "assistants": ["Ms. Green", "Mr. White"]
# # # # # #     },
# # # # # #     "students": ["John", "Jane", "Alice", "Bob"]
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'name of the second assistants: {university["faculty"]["assistants"][1]}')


# # # # # # # 4.Access and print the price of the third fruit.
# # # # # # store = {
# # # # # #     "fruits": [
# # # # # #         {"name": "apple", "price": 0.5},
# # # # # #         {"name": "banana", "price": 0.2},
# # # # # #         {"name": "cherry", "price": 1.5}
# # # # # #     ],
# # # # # #     "vegetables": [
# # # # # #         {"name": "carrot", "price": 0.3},
# # # # # #         {"name": "lettuce", "price": 1.0},
# # # # # #         {"name": "onion", "price": 0.4}
# # # # # #     ]
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'price of the third fruit: {store["fruits"][2]["price"]}')


# # # # # # #  5.Access and print the second non-fiction book.
# # # # # # library = {
# # # # # #     "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
# # # # # #     "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'second non-fiction book: {library["non-fiction"][1]}')

# # # # # # #  6.Access and print the age of the first child.
# # # # # # family = {
# # # # # #     "parents": ["John", "Jane"],
# # # # # #     "children": [
# # # # # #         {"name": "Tom", "age": 5},
# # # # # #         {"name": "Lucy", "age": 8}
# # # # # #     ]
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'age of the first child: {family["children"][0]["age"]}')


# # # # # # # 7.Access and print the name of the second main course.
# # # # # # restaurant = {
# # # # # #     "menu": {
# # # # # #         "appetizers": ["soup", "salad"],
# # # # # #         "main_courses": ["steak", "pasta"],
# # # # # #         "desserts": ["cake", "ice cream"]
# # # # # #     },
# # # # # #     "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'name of the second main course: {restaurant["menu"]["main_courses"][1]}')


# # # # # # #  8.Access and print the department of the user of the first desk.
# # # # # # workspace = {
# # # # # #     "desks": [
# # # # # #         {"user": "Alice", "department": "HR"},
# # # # # #         {"user": "Bob", "department": "Engineering"}
# # # # # #     ],
# # # # # #     "equipment": {"computers": 20, "printers": 10}
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'department of the user of the first desk: {workspace["desks"][0]["department"]}')
# # # # # # print(f'department of the user of the first desk: {workspace["desks"][0].get("department")}')


# # # # # # #  9.Access and print the name of the second designer.
# # # # # # team = {
# # # # # #     "developers": ["Dev A", "Dev B"],
# # # # # #     "designers": ["Designer X", "Designer Y"],
# # # # # #     "projects": ["Project 1", "Project 2"]
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'name of the second designer: {team["designers"][1]}')


# # # # # # #  10.Access and print the second international destination.
# # # # # # travel = {"domestic": ["Boston", "Chicago"], "international": ["Paris", "Tokyo"], "expenses": {"flights": 1500, "hotels": 2000}}
# # # # # # print("\n")
# # # # # # print(f'second international destination: {travel["international"][1]}')

# # # # # # # Assignment 2
# # # # # # # 1.Create a dictionary called `student` with keys "name", "age", and "grade", and 
# # # # # # # corresponding values "John", 20, and "A". Access and print the value of "name".
# # # # # # student = {"name": "John", "age": 20, "grade": "A"}
# # # # # # print("\n")
# # # # # # print(f'value of "name": {student["name"]}')

# # # # # # # 2.Create a dictionary called `product` with keys "name", "price", and "stock", and 
# # # # # # # corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
# # # # # # product = {"name": "Laptop", "price": 999.99, "stock": 50}
# # # # # # product["price"] = 899.99
# # # # # # print("\n")
# # # # # # print(f'Upadted value of "price": {product["price"]}')


# # # # # # # 3.Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
# # # # # # employee = {"name": "Alice", "position": "Manager"}
# # # # # # print("\n")
# # # # # # print("Before update", employee)
# # # # # # employee["salary"] = 50000
# # # # # # print("After updating with salary", employee)

# # # # # # # 4.Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
# # # # # # inventory = {"apple": 10, "banana": 5, "orange": 8 }
# # # # # # print("\n")
# # # # # # print("Before removing 'banana", inventory )
# # # # # # inventory.pop("banana")
# # # # # # print("After removing 'banana", inventory)

# # # # # # # 5.Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
# # # # # # person = {"name": "Bob", "age": 25, "city": "New York"}
# # # # # # print("\n")
# # # # # # person_copy = person.copy()
# # # # # # print('The new copy of person: ',person_copy)

# # # # # # # 6.Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
# # # # # # family = {
# # # # # #     "child1": {"name": "Ade", "age": 10},
# # # # # #     "child2": {"name": "Ayo", "age": 30},
# # # # # #     "child3": {"name": "John", "age": 90},
  
# # # # # # }
# # # # # # print("\n")
# # # # # # print(f'The age of "child2" is {family["child2"]["age"]}')
# # # # # # print(f'The age of "child2" is {family["child2"]["age"]}')


# # # # # # # 7.Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
# # # # # # car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

# # # # # # print("\n")
# # # # # # print(f'The value of "model" is {car["model"]}')


# # # # # # # 8.Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
# # # # # # settings = {"volume": 50, "brightness": 75, "language": "English"}
# # # # # # print("\n")
# # # # # # print('Settings:', settings)
# # # # # # settings["language"] = "Spanish"
# # # # # # print('Updated Settings:', settings)

# # # # # # # 9.Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
# # # # # # scores = {"math": 90, "Science": 85, "English": 88}
# # # # # # print("\n")
# # # # # # print('Before removal:', scores)
# # # # # # scores.pop("Science")
# # # # # # print('After removing the key "Science":', scores)


# # # # # # # 10.Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
# # # # # # print("\n")
# # # # # # menu = {"starter": "Soup", "main_course": "Steak", "dessert": "Ice Cream"}
# # # # # # print(f'Is "appetizer" present in menu: {"appetizer" in menu} ')

# # # # # # # # 11.Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
# # # # # # # config = {"theme": "dark", "language": "English", "timezone": "UTC"}
# # # # # # # print("\n")
# # # # # # # config.clear()
# # # # # # # print(config)


# # # # # # # # 12.Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# # # # # # # # "Charlie", and corresponding phone numbers as values. Print the number of 
# # # # # # # # items in the dictionary.
# # # # # # # phone_book = {"Alice": 123908988, "Bob": 64746475656565, "Charlie": 57464746474646 }
# # # # # # # print("\n")
# # # # # # # print(len(phone_book))

# # # # # # # # 13.Create a dictionary called `grades` with keys "math", "science", and "history", 
# # # # # # # # and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# # # # # # # # dictionary.

# # # # # # # # 14.Create a dictionary called `employee` with keys "name", "position", and 
# # # # # # # # "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# # # # # # # # of all the values in the dictionary.

# # # # # # # # 15.Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# # # # # # # # corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# # # # # # # # key-value pairs in the dictionary.



# # # # # # # 28/4/25
# # # # # # # SET
# # # # # # # Assignment

# # # # # # # Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in 
# # # # # # # the set and print the result.
# # # # # # print("\n")
# # # # # # fruits =  {"air", "water", "food"}
# # # # # # print(f'{"food" in fruits} "food" is in the set')

# # # # # # # Create a set called colors with values {"red", "green", "blue"}. Add the color "yellow" 
# # # # # # # to the set and print the updated set.
# # # # # # colors = {"red", "green", "blue"}
# # # # # # print("\n")
# # # # # # colors.add("yellow")
# # # # # # print(f'Updated set: {colors}')

# # # # # # # Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to the set and print the updated set.
# # # # # # animals = {"cat", "dog", "rabbit"}
# # # # # # animals.update(["horse", "sheep"])
# # # # # # print("\n")
# # # # # # print(f'Updated Set: {animals}')

# # # # # # # Create a set called countries with values {"USA", "Canada", "Mexico"}. Remove "Canada" from the set and print the updated set.
# # # # # # countries = {"USA", "Canada", "Mexico"}
# # # # # # print("\n")
# # # # # # countries.remove("Canada")
# # # # # # print(f'Updated Set after removing Canada: {countries}')

# # # # # # # Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in the set without raising an error.
# # # # # # cities = {"New York", "Los Angeles", "Chicago"}
# # # # # # cities.discard("Houston")
# # # # # # print("\n")
# # # # # # print(f'Updated Set after removing Houston which is not in the set without raising an error: {cities}')

# # # # # # # Given the list seasons = ["Spring", "Summer", "Fall", "Winter", “Spring”], convert the list to a set to get rid of the duplicate `Spring`.
# # # # # # seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
# # # # # # seasons = set(seasons)
# # # # # # print("\n")
# # # # # # print("Updated seasons set:", seasons)

# # # # # # # Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets and print the result.
# # # # # # set1 = {1, 2, 3}
# # # # # # set2 = {3, 4, 5}
# # # # # # set3 = set1.union(set2)
# # # # # # print("\n")
# # # # # # print("The union of set1 and set2 is", set3)

# # # # # # # Given two sets, setA = {"a", "b", "c"} and setB = {"c", "d", "e"}, find the intersection of the sets and print the result.
# # # # # # setA = {"a", "b", "c"}
# # # # # # setB = {"c", "d", "e"}
# # # # # # intersecsion = setA.intersection(setB)
# # # # # # print("\n")
# # # # # # print("The intersection of setA and setB is", intersecsion)

# # # # # # # Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print the updated set.
# # # # # # prime_numbers = {2, 3, 5, 7}
# # # # # # prime_numbers.add(11)
# # # # # # print("\n")
# # # # # # print("Updated Set:", prime_numbers)

# # # # # # # # Given the set odd_numbers = {1, 3, 5, 7, 9}, remove a random item from the set and print the updated set.
# # # # # # # odd_numbers = {1, 3, 5, 7, 9}
# # # # # # # odd_numbers.pop()
# # # # # # # print("\n")
# # # # # # # print("Updated Set after removing a random item:", odd_numbers)

# # # # # # # # Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result.
# # # # # # # vowels = {"a", "e", "i", "o", "u"}
# # # # # # # vowels.clear()
# # # # # # # print("\n")
# # # # # # # print("Empty vowel set:", vowels)

# # # # # # # # Given the set letters = {"a", "b", "c"}, find the difference between `letters` and another set {"b", "c", "d"}. Print the result. Afterwards, find the symmetric difference and print the result.
# # # # # # # letters = {"a", "b", "c"}
# # # # # # # letter2 = {"b", "c", "d"}
# # # # # # # print("\n")
# # # # # # # print(f'difference between `letters` and letters2: {letters.difference(letter2)}')
# # # # # # # print(f'symmetric difference between `letters` and letters2: {letters.symmetric_difference(letter2)}')

# # # # # # # # Create a set called tech_brands with values {"Apple", "Google", "Microsoft"}. 
# # # # # # # # Add the items from another set {"Amazon", "Facebook"} and print the updated set tech_brands without creating a new set.
# # # # # # # tech_brands = {"Apple", "Google", "Microsoft"}
# # # # # # # brands2 = {"Amazon", "Facebook"}
# # # # # # # tech_brands.update(brands2)
# # # # # # # print("\n")
# # # # # # # print("\n")
# # # # # # # print(f'Updated Tech_brands: {tech_brands}')

# # # # # # # # Create a set called students with values {"Alice", "Bob", "Charlie", "David"}. Use the remove method to remove "Charlie" from the set and print the updated set. Then try to remove "Eve" from the set and observe the behavior.
# # # # # # # students = {"Alice", "Bob", "Charlie", "David"}
# # # # # # # students.remove("Charlie")
# # # # # # # print("\n")
# # # # # # # print("Updated set after removing Charlie:",students)
# # # # # # # # students.remove("Eve")
# # # # # # # # print("Updated set after removing Eve:",students)

# # # # # # # # Given a list numbers_list = [1, 2, 3, 4, 4, 5, 5], convert this list to a set to remove 
# # # # # # # # duplicates and print the resulting set.
# # # # # # # numbers_list = [1, 2, 3, 4, 4, 5, 5]
# # # # # # # numbers_list = set(numbers_list)
# # # # # # # print("\n")
# # # # # # # print("Converted list:", numbers_list)
# # # # # # # numbers_list = set(numbers_list)

# # # # # # # # Given a string text = "hello", convert this string to a set to find the unique 
# # # # # # # # characters and print the resulting set.
# # # # # # # text = "hello"
# # # # # # # text = set(text)
# # # # # # # print("\n")
# # # # # # # print("Converted Set:", text)

# # # # # # # # Create a set called vehicles with values {"car", "bike", "bus", "train"}. Find out how 
# # # # # # # # many items are in the set and print the result.
# # # # # # # vehicles = {"car", "bike", "bus", "train"}
# # # # # # # print("\n")
# # # # # # # print("Amount of items in the set is", len(vehicles))

# # # # # # # # Given the set gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}, print the 
# # # # # # # # number of items in the set.
# # # # # # # gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}
# # # # # # # print("\n")
# # # # # # # print("Amount of items in the set is", len(gadgets))



# # # # # # # 29/4/25
# # # # # # # Assignment


# # # # # # # 1.Collect two numbers as input from the user and assign as variables, a and b, write an if statement that prints "a and b are both positive" if both a and b are positive, prints "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# # # # # # # neither is positive.
# # # # # # a = int(input("Enter first number: "))
# # # # # # b = int(input("Enter Second number: "))
# # # # # # if a > 0 and b > 0:
# # # # # #     print(' a and b are both positive')
# # # # # # elif  a > 0 or b > 0:
# # # # # #     print('Only one is positive')
# # # # # # else:
# # # # # #     print('Neither is positive')


# # # # # # #2.Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# # # # # # three_numbers = input('Enter three random numbers seperated by comma: ').split(",")
# # # # # # x,y,z = three_numbers

# # # # # # if int(z) > int(x) < int(y) and int(z) > int(y) > int(x):
# # # # # #     print("Increasing order")
# # # # # # elif int(z) < int(x) > int(y) and int(z) < int(y) < int(x): 
# # # # # #     print("Decreasing order")
# # # # # # else:
# # # # # #     print("Neither")

# # # # # # #3.Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# # # # # # palindrome = input("Enter a word: ").replace(" ", "").lower()
# # # # # # if palindrome == palindrome[::-1]:
# # # # # #     print("Is a palindrome")
# # # # # # else:
# # # # # #     print("Not a palindrome")


# # # # # # #4.You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
# # # # # # x = input("Enter a variable for 'x': ")
# # # # # # y = input("Enter a variable for 'y': ")
# # # # # # z = input("Enter a variable for 'z': ")

# # # # # # if  z == x == y:
# # # # # #     print("All same")
# # # # # # elif x == y or y == z or z == x:
# # # # # #     print("Two are equal")
# # # # # # else:
# # # # # #     print("All different")

# # # # # # #5.Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".
# # # # # # angle1 = int(input("Enter first angle: "))
# # # # # # angle2 =int( input("Enter second angle: "))
# # # # # # angle3 = int(input("Enter third angle: "))
# # # # # # if angle1 + angle2 + angle3 == 180:
# # # # # #     if angle1 < 0 or angle2 < 0 or angle3 < 0:
# # # # # #         print("invalid triangle")
# # # # # #     else:
# # # # # #         print("Valid triangle")
# # # # # # else:
# # # # # #     print("Invalid triangle")


# # # # # # #6.You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.
# # # # # # ch = input("Enter an alphabet: ").strip().lower()
# # # # # # if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
# # # # # #     print(ch, "is a Vowel")
# # # # # # else:
# # # # # #     print(ch, "is a consonant")



# # # # # # 7.Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".
# # # # # # colorss = input("Enter three colors seperated by commas: ").split
# # # # # # if colorss[0] 

# # # # # # #9.Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".

# # # # # # message = input("Enter your message: ").lower().split(" ")
# # # # # # if "urgent" in message or "important" in message or "immediate" in message:
# # # # # #     print("High priority message")
# # # # # # else:
# # # # # #     print("Normal message")


# # # # # # #10.You have two variables, status1 and status2, provided through user input, each of which can be "active", “inactive", or "pending". Write an if statement to print "Both active" if both statuses are "active", "One active" if exactly one is "active", and "None active" if neither is "active"
# # # # # # status1 = input("Enter first status 'active, inactive or pending': ")
# # # # # # status2 = input("Enter second status 'active, inactive or pending': ")
# # # # # # if status1 == "active" and status2 == "active":
# # # # # #     print("Both active")
# # # # # # elif status1 == "active" or status2 == "active":
# # # # # #     print("One active")
# # # # # # else:
# # # # # #     print("None active")


# # # # # # # 11.Given a string `filename` supplied by the user, write an if statement to check if the filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise print "Not an image file".
# # # # # # filename = input("Enter filename: ")
# # # # # # if ".jpg" in filename or ".png" in filename or ".gif" in filename:
# # # # # #     print("Image file")
# # # # # # else:
# # # # # #     print("Not an image file")


# # # # # # # 12.You have a variable `access_level` provided through user input which can be "admin","user", or "guest". Write an if statement that prints "Full access" if access_level is "admin", "Limited access" if it is "user", and "No access" if it is "guest".
# # # # # # access_level = input("Enter your access level: ")
# # # # # # if access_level == "admin":
# # # # # #     print("Full access")
# # # # # # elif access_level == "user":
# # # # # #     print("Limited access")
# # # # # # elif access_level == "guest":
# # # # # #     print("No access")
# # # # # # else:
# # # # # #     print("Invalid Entry")


# # # # # # # 13.Given a string `email` collected from the user, write an if statement to check if the email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise print "Invalid email".
# # # # # # email = input("Enter your email: ")
# # # # # # if "@" in email and "." in email:
# # # # # #     print("Valid email")
# # # # # # else:
# # # # # #     print("Invalid email")


# # # # # # # 14.You have a variable `day` provided by user input which can be any day of the week (e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# # # # # # day = input("Enter any day of the week: ").lower()
# # # # # # if day == "Satuday" or day == "Sunday":
# # # # # #     print("Weekend")
# # # # # # else:
# # # # # #     print("Weekday")


# # # # # # 15.Write a program that takes three numbers (num1, num2, num3) as a comma-separated string input from the user and prints the greatest number. Use conditional statements to determine which number is the greatest. Bonus point if you can do it without `else` statements.
# # # # # # numbers = input("Enter num1, num2, num3 seperated by commas: ").split(",")
# # # # # # if numbers[0] > numbers[1] and numbers[0] > numbers[2]:
# # # # # #     print(numbers[0],'is the greatest')
# # # # # # elif  numbers[1] > numbers[0] and numbers[1] > numbers[2]:
# # # # # #     print(numbers[1],'is the greatest')
# # # # # # elif  numbers[2] > numbers[0] and numbers[2] > numbers[1]:
# # # # # #     print(numbers[2],'is the greatest')

# # # # # # Time Table LOOPS

# # # # # # i = int(input("Enter a number: "))
# # # # # # j = 1
# # # # # # while j <= 12:
# # # # # #     print(f'{i} x {j} = {i*j}')
# # # # # #     j += 1



















# # # # # # Assignments On While Loops

# # # # # # 1.Write a program that uses a while loop to print numbers from 1 to 10.
# # # # # # i = 1
# # # # # # while i <= 10:
# # # # # #     print(i)
# # # # # #     i += 1

# # # # # # 2.Write a program that takes an integer n from the user and calculates the sum of all 
# # # # # # natural numbers up to n using a while loop.
# # # # # # n = int(input("Enter a number: "))
# # # # # # i = 1
# # # # # # sum = 0
# # # # # # while i <= n:
# # # # # #     sum += i
# # # # # #     i += 1
    
# # # # # # print(sum)



# # # # # # 3.Write a program that generates a random number between 1 and 50. Use a while loop to allow 
# # # # # # the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low.


# # # # # #4.Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# # # # # # correct_password = 'secret'
# # # # # # while True:
# # # # # #     pass_key = input("Enter your password: ")
# # # # # #     if pass_key == correct_password:
# # # # # #         print("Correct Password")
# # # # # #         break
# # # # # #     else:
# # # # # #         print("Incorrect Password")
    

# # # # # # 5.Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
# # # # # # number = int(input("Enter an Integer: "))
# # # # # # while number >= 0:
# # # # # #     print(number)
# # # # # #     number -=  1




# # # # # # 6.Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# # # # # # n = int(input("Enter an Integer: "))
# # # # # # i = 1
# # # # # # while i <= n: 
# # # # # #     if i % 2 == 0:
# # # # # #         print(i)
# # # # # #     i += 1


# # # # # # 7.Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# # # # # # Sample Input:
# # # # # # Enter the base: 2
# # # # # # Enter the exponent: 3
# # # # # # Output:
# # # # # # # 2 raised to the power of 3 is 8
# # # # # # # Sample Input:
# # # # # # # Enter the base: 5
# # # # # # # Enter the exponent: 4
# # # # # # # Output:
# # # # # # # 5 raised to the power of 4 is 625
# # # # # # base = int(input("Enter your Base: "))
# # # # # # exponent = int(input("Enter your exponent: "))
# # # # # # i = 1
# # # # # # base_1 = base
# # # # # # while i <= exponent:
# # # # # #     base_1 *= base
# # # # # #     i += i
# # # # # # print(f'{base} raised to the power of {exponent} is {base_1}')
 

# # # # # # 8.Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.
# # # # # # string = input("Enter a string: ").lower()
# # # # # # vowels = ('a','e', 'i', 'o', 'u')
# # # # # # index = 0
# # # # # # no_of_vowels = 0
# # # # # # j = 1
# # # # # # while j < len(string):
# # # # # #     if string[index] in vowels:
# # # # # #         no_of_vowels += 1
# # # # # #     index += 1
# # # # # #     j += 1
# # # # # # print("no of vowels in the string is", no_of_vowels)

# # # # # # 9.Write a program that takes a string input from the user and uses a while loop to reverse the string.
# # # # # # strings = input("Enter a string: ")
# # # # # # reverse_strings = ""
# # # # # # index = len(strings)-1
# # # # # # while index >= 0:
# # # # # #     reverse_strings += f"{strings[index]}"
# # # # # #     index -= 1
    
# # # # # # print(reverse_strings)

# # # # # # Write a program that takes comma-separated integers from the user, converts that
# # # # # # 	to a tuple and uses a while loop to find the minimum value in the tuple.
# # # # # #  11. 	Write a program that takes a string input from the user and uses a while loop to count
# # # # # # 	the occurrences of each character, storing the counts in a dictionary.
# # # # # # 	Sample Input:
# # # # # # 	Enter a string: Hello
# # # # # # 	Sample Output:
# # # # # # 	{‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}






# # # # # # 7/5/2025
# # # # # # For loops ASSIGNMENT

# # # # # # 1.Write a program that takes an integer input from the user and uses a loop to calculate 
# # # # # # the sum of its digits. Print the sum. Example:
# # # # # # Input: 1234
# # # # # # Output: 10 (1+2+3+4)
# # # # # # numbers = list((input("Enter an interger: ")))
# # # # # # sum = 0
# # # # # # for number in numbers:
# # # # # #     sum += int(number)

# # # # # # print("Sum of numbers is",sum)
    

# # # # # # 2.Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# # # # # # Input: "hello world"
# # # # # # Output: Vowels: 3, Consonants: 7

# # # # # # string = input("Enter a string: ")
# # # # # # vowels = ('aeiou')
# # # # # # vowel_count = 0
# # # # # # consonant_count = 0
# # # # # # for char in string:
# # # # # #     if char in vowels:
# # # # # #         vowel_count += 1
# # # # # #     else:
# # # # # #         consonant_count += 1
# # # # # # print(f'Output: Vowels: {vowel_count}, Consonants: {consonant_count}')


# # # # # #3.Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# # # # # # Input: 5
# # # # # # Output:
# # # # # # 5 x 1 = 5
# # # # # # 5 x 2 = 10
# # # # # # 5 x 3 = 15
# # # # # # ...
# # # # # # 5 x 12 = 60
# # # # # # number = int(input('Enter a number: '))
# # # # # # for i in range(1, 13):
# # # # # #     print(f'{number} x {i} = {number * i}')


# # # # # #4.Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# # # # # # Example:
# # # # # # Input: "python"
# # # # # # Output: "nohtyp"
# # # # # # strings = input("Enter a word: ")
# # # # # # index = len(strings)
# # # # # # for string in strings:
# # # # # #     index -= 1
# # # # # #     print(strings[index])




# # # # # # 5.Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# # # # # # Input: "1, 2, 3, 2, 4, 3"
# # # # # # Output: [1, 2, 3, 4]
# # # # # # numbers = list(input("Enter your comma sepearted values: "))
# # # # # # unique_numbers = []
# # # # # # for num in numbers:
# # # # # #     if num not in unique_numbers:
# # # # # #         unique_numbers.append(num)
# # # # # # print(f"new list with no duplicate is {unique_numbers}")

# # # # # # 6.Write a program that takes an integer input n from the user and prints the first 
# # # # # # 	n numbers in the Fibonacci sequence. Example:
# # # # # # 	Input: 10
# # # # # # 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# # # # # # n = (int(input("Enter an integer: ")))
# # # # # # output = []



# # # # # #  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# # # # # # 	loop to find and print the largest number in the list. Don’t use the built-in max 
# # # # # # 	function or anything similar.
# # # # # # 	Input: "10, 20, 5, 15"
# # # # # # 	Output: 20

# # # # # #  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# # # # # # 	even numbers from 1 to n. Print the sum.
# # # # # # 	Input: 10
# # # # # # 	Output: 30 (2 + 4 + 6 + 8 + 10)
# # # # # # n = int(input("Enter an integer: "))
# # # # # # even_sum = 0
# # # # # # sum = ""
# # # # # # for i in range(2, n+1, 2):
# # # # # #     even_sum += i
# # # # # #     if i == 2:
# # # # # #        sum += f'{i}'
# # # # # #     else:
# # # # # #       sum += f' + {i}'

    
# # # # # # print("Output: ", even_sum, f'({sum})')
   
# # # # # #  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# # # # # # 	in the string. Print each character along with its frequency. Example:
# # # # # # 	Input: "hello"
# # # # # # 	Output:
# # # # # # h: 1
# # # # # # e: 1
# # # # # # l: 2
# # # # # # o: 1


# # # # # # 10.Write a program that takes an integer n from the user and calculates the sum of 
# # # # # # 	squares of all numbers from 1 to n. Print the sum. Example:
# # # # # # 	Input: 3
# # # # # # 	Output: 14 (1^2 + 2^2 + 3^2)
# # # # # number = int(input("Enter an integer: "))
# # # # # sum_nsquare = 0
# # # # # num_square = ""
# # # # # for num in range(1, number+1):
# # # # #   sum_nsquare += num**2
# # # # #   num_square += f'{num}^2 +'
# # # # # print("Output: ",sum_nsquare, num_square)
    



# # # # # #  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# # # # # # 	letter of each word. Print the acronym. Example:
# # # # # # 	Input: "Portable Network Graphics"
# # # # # # 	Output: "PNG"
# # # # # #  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# # # # # # 	Print the count. Example:
# # # # # # 	Input: "Hello world from Python"
# # # # # # 	Output: 4
# # # # # #  13. 	Collect a string from the user and only print put the words that start with the letter 
# # # # # # 	‘S’. Example:
# # # # # # 	Input: “Print only the words that start with s in this sentence”
# # # # # # 	Output: 
# # # # # # 	start
# # # # # # 	s
# # # # # # 	Sentence
# # # # # #  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.
# # # # # #  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# # # # # # 	by 3.







# # # # # # # Functions
# # # # # # 1.Write a function sum_numbers(a, b) that returns the sum of two numbers.
# # # # # def sum_numbers(a, b):
  
# # # # #     print(f'sum of {a} and {b} is {a + b}')
  
  
# # # # # num1 = int(input('Enter int for a: '))
# # # # # num2 = int(input('Enter int for b: '))
# # # # # sum_numbers(num1, num2)

# # # # # 2. Write a function is_even(n) that returns True if n is even and False if n is odd.
# # # # # def is_even(num):
# # # # #     if num % 2 == 0:
# # # # #       print(f'TRUE {num} is even')
# # # # #     else:
# # # # #      print(f'FALSE {num} is odd')

# # # # # num1 = int(input('Enter a number: '))   
# # # # # is_even(num1)
    
# # # # #3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# # # # def is_prime(num):
# # # #   for i in range(2, num):
# # # #     if num % i == 0:
# # # #       return False
      
# # # #   else:
# # # #     return True

# # # # # num1 = int(input('Enter a number: ')) 
# # # # # is_prime(num1)  

# # # # # 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# # # # def is_all_prime(num):
# # # #     for i in range(2, num + 1):
# # # #       if is_prime(i):
# # # #         print(i, end =' ')

# # # # num1 = int(input('Enter a number: ')) 
# # # # is_all_prime(num1) 

    
# # # # # Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# # # # def lesser_of_two_evens(a, b):
# # # #   if a % 2 == 0 and b % 2 == 0:
# # # #     return min([a, b])
      
# # # #   elif a % 2 != 0 or b % 2 != 0:
# # # #     return max([a, b])
    



  
  
  
    
    
      

      
          


# # # # # Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# # # # # is_alliteration(‘Levelheaded llama’) —> True
# # # # # is_alliteration(‘Crazy Kangaroo’) –> False
# # # # # Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# # # # # old_macdonald(‘macdonald’) —> MacDonald
# # # # # Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# # # # # Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# # # # # spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# # # # # spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# # # # # spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
# # # # # Write a function vol(radius) that computes the volume of a sphere given its radius.
# # # # # Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).






# # # # ASSIGNMENT OOP
# # # # ACCOUNTANT

# # # class Account:
# # #     def __init__(self, owner, balance):
# # #         self.owner = owner
# # #         self.balance = balance

# # #     def deposit(self, amount):
# # #         self.balance += amount  
# # #         print(f'{amount} has been sucessfully Deposited.\nBalance: {self.balance}')
        
    
# # #     def withdraw(self, amount):
# # #         if self.balance > amount:
# # #           self.balance -= amount
# # #           print(f'{amount} has ben sucessfully withdrawn.\nBalance: {self.balance}')
# # #         else:
# # #             print(f'Insufficient Funds!!!!!!')
            

  

# # # acct1 = Account("Winnie", 6000) 
# # # print(f'Account Owner: {acct1.owner}\nAccount balance: {acct1.balance}')
# # # acct1.deposit(50)
# # # acct1.withdraw(15)
# # # acct1.withdraw(7000)

# # print('Instruction: Pick an option a to d for the following questions.')
# # for question in questions_bank:
# #     print(f'{question['question']}\n{question['option']}')
# #     option = input('pick a answer within a to d: ')
# #     if option == question['answer']:
# #         count += 1
# # print(f'Your total score is: {count}')      


        

    





# # ASSIGNMENT
# # PACKAGES, MODULES, LIBRARIES
# # WEB SCRABING
# # QUOTE DATA ANALYSER


# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint

# url = 'http://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# all_quotes = soup.find_all('div', 'quote')

# quotes_full_data = []

# for quote in all_quotes:

#     quote_text = quote.find('span', 'text').get_text()
#     quote_author = quote.find('small', 'author').get_text()
#     quote_tags = quote.find_all('a', 'tag')

#     quote_tags = [tag.get_text() for tag in quote_tags]

#     quote_data = {"name": quote_author, "quote": quote_text, "tags": quote_tags }

#     quotes_full_data.append(quote_data)
#     # authors.append(quote_author)


# # print('All our quotes: ', all_quotes)
# # print("Authors: ", list(set(authors)))


# # print(quotes_full_data)

# count_num_of_is = 0
# tag_list = []

# for quote in quotes_full_data:
#     if 'is' in quote['quote'].lower():
#         count_num_of_is += 1

#     for t in quote['tags']:
#         tag_list.append(t)


# print('Number of is: ', count_num_of_is)   
# print(tag_list)


# ASSIGNMENT
# COUNTRY ANALYSER

import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/' 
try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)
    all_countries = soup.find_all('div', 'col-md-4 country')
    list_of_countries = []

    for country_data in all_countries:
        country_name = country_data.find('h3', 'country-name').get_text().strip()
        capital_name = country_data.find('span', 'country-capital').get_text().strip()
        population = country_data.find('span', 'country-population').get_text().strip()
        area_size = country_data.find('span', 'country-area').get_text().strip()
        country_data = {'country': country_name, 'capital': capital_name, 'population': int(population), 'area_size': int(float(area_size))}
        list_of_countries.append(country_data)

    max_pop_country_name, max_country_pop = list_of_countries[0]['country'], list_of_countries[0]['population']
    min_pop_country_name, min_country_pop = list_of_countries[0]['country'], list_of_countries[0]['population']
    total_pop = 0
    list_of_pop_density = []
    list_of_countries_starting_A = []
    countries_greater_than_1_000_000km = []
    countries_less_than_500km = []
    countries_pop_lessthan_0 = []
    
    for country in list_of_countries:
        if country['population'] > max_country_pop:
            max_country_pop = country['population']
            max_pop_country_name = country['country']
        if country['population'] < min_country_pop:
            min_country_pop = country['population']
            min_pop_country_name = country['country']
        total_pop += country['population']  
        if country['area_size'] != 0:
            country_den = country['population'] / country['area_size']
            density_data = {'name': country['country'], 'density': country_den }
            list_of_pop_density.append(density_data)
        elif country['area_size'] == 0:
            country_den = 0
            density_data = {'name': country['country'], 'density': country_den}
            list_of_pop_density.append(density_data)
        if country['country'][0] =='A':
           list_of_countries_starting_A.append({'name': country['country'], 'capital': country['capital']})
        if country['area_size'] > 1000000:
            countries_greater_than_1_000_000km.append(country['country'])
        elif country['area_size'] < 500:
            countries_less_than_500km.append(country['country'])
        if country['population'] == 0:
            countries_pop_lessthan_0.append(country['country'])




       
    
       
        
            

        
    
     

    print(max_pop_country_name)
    print(max_country_pop)
    print(min_pop_country_name)
    print(min_country_pop)
    print(f'The average population of all countries is {total_pop // len(list_of_countries)}')
    print(f'List of country\'s density and their names:\n {list_of_pop_density}')
    print(f'List of countries starting with A and thier capitals: \n {list_of_countries_starting_A}')
    print(f'List of countries with area_size graeter than 1000,000km^2:\n {countries_greater_than_1_000_000km}')
    print(f'List of countries with area_size less than 500km^2:\n {countries_less_than_500km}')
    print(f'List of countries with population 0: \n {countries_pop_lessthan_0}')
    

except requests.exceptions.RequestException:
    print('Network connection issue')



              
              
    
    
    


    
# print(f'The Total Number of all countries: {len(list_of_countries)}')
# print()

    

    


















































































