questions_bank = [{'question': '1. What is 2 + 2?', 'answer': 'b', 'option': 'a). 3\nb). 4\nc). 5 \nd). 6'},
{'question': '\n2. What color is the sky on a clear day?', 'answer': 'b', 'option': 'a). Red\nb). Blue\nc). Green\nd). Yellow'}, 
{'question': '\n3. How many legs does a spider have? ', 'answer': 'a', 'option': 'a). 6\nb). 7\nc). 8\nd). 9'},
{'question': '\n4. What sound does a cow make? ', 'answer': 'c', 'option': 'a). Meow\nb). Bark\nc). moo\nd). quack'},
{'question': '\n5. What is the opposite of hot? ', 'answer': 'b', 'option': 'a). Warm\nb). Cold\nc). Cool\nd). Boiling'}]
 

count = 0
names = ['Akeem Adenuga', 'Wole Soyinka', 'Fel Kuti', 'Yinka Quadri']
while True:
    fullname = input('Enter your Fullname: ')
    if fullname in names: 
        print(f'\nWelcome', fullname)
    else:
        continue

    print(f'\nInstruction: Pick an option a to d for the following questions.')
    for question in questions_bank:
        print(f'{question['question']}\n{question['option']}')
        option = input('\npick a answer within a to d: ')
        if option == question['answer']:
            count += 1
    print(f'At the end of the CBT exam, you scored {count} points.')    

