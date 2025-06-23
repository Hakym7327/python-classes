# first_set = {"Tobi", "James", "John", "James", "Johnny", "james", 40, 829, 20, 21, True, False, 0, 1}

# print('Our suet: ', first_set)

# first_set = {"Tobi", "James", "John", "James", "Johnny", "james"}

# print('Item: ', first_set)

# first_set.add("Tobi Dada")
# first_set.add("Tobi Dada")
# first_set.add("Tobi Dada")
# first_set.add("Tobi Dada")


# print('Now, the set: ', first_set)

# first_set.remove("John")
# first_set.remove("James")
# print('Updated set: ', first_set)

# print('Number of  items in set are: ', len(first_set))


# distinct_names = {"Johnny Bravo", "Raymond", "Altman"}

# other_names = {"ChatGPT", "Vitalik", "Nick", "Altman", "Altman"}

# print('Distinct names: ', distinct_names)

# distinct_names.update(other_names)

# print('Updated names: ', distinct_names)
# # Does not throw an error when this item does not exist
# distinct_names.discard("Wale")



# animals = {"Cheetah", "Hippo", "Rhino", "Lion", "Tiger"}

# one_animal = list(animals).remove("")
# print('Animal: ', one_animal)



# animals = {"Cheetah", "Hippo", "Rhino", "Lion", "Tiger"}
# animals.clear()

# print(type(animals))



# animals = {"Cheetah", "Hippo", "Rhino", "Lion", "Tiger"}
# animals2 = {"Dog", "Cat", "Penguin", "Cheetah"}
# dogs = {"Border Collie", "Bingo", "German Shepherd", "Chihuahua", "Bulldog"}



# all_animals = animals.union(animals2)
# print('All animals: ', all_animals)

# print(animals)

# animals = animals.union(animals2)
# print(animals)


# animals.update()


# All animals that exist in both collections

# print(animals.intersection(animals2))

# Retrieve all animals that only the animal variable has
# print(animals2.difference(animals))

# Retrive what is unique to both sets
# print(animals)
# print(animals2)
# print('Sym: ', animals.symmetric_difference(animals2))


# THis throws TypeError because the symbol will not be allowed between operands that are not set
# print(animals & list(animals2))
# print(animals.intersection(list(animals2)))


# print(animals  - (animals2))




# animals = {"Cheetah", "Hippo", "Rhino", "Lion", "Tiger"}
# animals2 = {"Dog", "Cat", "Penguin", "Cheetah"}
# dogs = {"Border Collie", "Bingo", "German Shepherd", "Chihuahua", "Bulldog"}

# all_animals = animals | animals2 | dogs
# common_animals = animals.intersection(animals2).intersection(dogs)
# common_animals = animals & animals2 & dogs

# print('All: ', all_animals)
# print('Common animals: ', common_animals)



# animals = {"Cheetah", "Hippo", "Rhino", "Lion", "Tiger"}
# animals2 = {"Dog", "Cat", "Penguin", "Cheetah"}



animals = {"Dog", "Cat", "Penguin", "Cheetah", "Bingo", "Bulldog"}
dogs = {"Border Collie", "Bingo", "German Shepherd", "Chihuahua", "Bulldog"}

# animals.difference_update(dogs)

# animals = animals.difference(dogs)
# print(animals)

# animals.symmetric_difference_update(dogs)
# print('Animals: ', animals)
# dog, cat, penguin, cheetah



# animals = {"Dog", "Cat", "Penguin", "Cheetah", "Bingo", "Bulldog"}
# dogs = {"Border Collie",  "German Shepherd", "Chihuahua",}

# # animals.difference_update(dogs)
# # print(animals)

# print(dogs.isdisjoint(animals))


# setA = {3, 5, 234, 65, 2, 5, 7, 9}

# setB = { 3, 7}

# print(setA.issubset(setA))


customers = {"Tobi", "James", "Niko", "Hakeem", "Gray", "Sodiq", "Seun"}

depositors = {"Tobi", "Hakeem", "Seun"}
borrowers = {"Tobi", "Seun", "Niko", "James"}

# Niko, James, Sodiq, Gray

# Let's find those who  have both borrowed and also deposited before
print('Those who have both borrowed and deposited are: ', depositors.intersection(borrowers))

all_borrowers_and_depositors = depositors.union(borrowers)

inactive_customers = customers.difference(all_borrowers_and_depositors)

print('All inactive customers: ', inactive_customers)

# Customers who only borrowed
print('Those who borrowed alone: ')
print(borrowers.difference(depositors)) 
print(depositors.difference(borrowers)) 

# Customers who never deposited
print(customers.difference(depositors))



customers = {"Tobi", "James", "Niko", "Hakeem", "Gray", "Sodiq", "Seun"}

depositors = {"Tobi", "Hakeem", "Seun"}
borrowers = {"Tobi", "Seun", "Niko", "James"}


# Customers who never deposited, but may have borrowed or not
borrowers_that_did_not_deposit = borrowers.difference(depositors)
inactive_customers_not_deposit = customers.difference(depositors)
print("ANswer:  ", inactive_customers_not_deposit.union(borrowers_that_did_not_deposit))


# Create a list called "days of the week", containing "Monday", "Wednesday", "Wednesday", "Friday", "Monday". Get a list of the days of the week without repetition




