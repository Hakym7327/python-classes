17/4/2025

# Assignnment 2

# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 2
waitlist.extend(["Ken", "Jack", "Ivy"])
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 3
waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 4
confirmed_guests.remove("Alice")
waitlist.remove('Ken')
confirmed_guests.insert(0, 'Ken')
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 5
print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print('Charlie' in confirmed_guests, 'Charlie is confirmed')

# Stage 6
confirmed_guests.remove('David')
confirmed_guests.remove('Eve')
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 7
waitlist.remove('Jack')
waitlist.remove('Ivy')
confirmed_guests.append('Jack')
confirmed_guests.append('Ivy')
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 8
waitlist.remove('Oliver')
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 9
print("\n\nStage 9")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print('The last three guest on the guest list are:', confirmed_guests[-3:])


# Stage 10
waitlist.remove('Noah')
confirmed_guests.append('Noah')
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 11
print("\n\nStage 11")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print('The total number of people attending the wedding is',len(confirmed_guests))


# Stage 12
print("\n\nStage 12")
print('Here is the list of our Confirmed Guests:', confirmed_guests)


# Stage 13
print("\n\nStage 13")
confirmed_guests.sort()
confirmed_guests[3] = 'Collins'
confirmed_guests.remove('Noah')
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 14
print("\n\nStage 14")
guest_list_for_caterer = confirmed_guests.copy()
print('Here is a copy of the confirmed guest list:', guest_list_for_caterer)


# Stage 15
print("\n\nStage 15")
waitlist.clear()
print('Waitlist is cleared:', waitlist)







