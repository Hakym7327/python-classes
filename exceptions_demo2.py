

# Write a program that takes two numbers and divides the first one by the second number and displ;ay the output

# try:
#     num1 = int(input('Enter number:  ')) # value error
#     num2 = int(input('Enter number:  ')) # value error
#     print(num1 / num2) # zero division error

# except:
#     print("Okay, I guess you entered wrong value somewhere.")
    
# print('Finished.')




mydict = {
    'name' : "Tobi",
    "course": "CSC",
    "gender": "Male"
}


try:
    del mydict['names']
except:
    pass # handle the error and don't do anything. [Fail silently]

print(mydict)


