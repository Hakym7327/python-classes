question_bank = [{'question': '1. What is the function of an operating system?', 
'keywords': ["resource management", "process management", "memory management", "interface", "hardware"]},
{"question": "2. Explain the concept of object-oriented programming (OOP).", "keywords": ["class", "object", "inheritance", "polymorphism", "encapsulation"]},
{"question": "3. What are the advantages of using databases?","keywords": ["data integrity", "data security", "redundancy", "data sharing", "consistency"]},
{"question": "4. Describe the role of a compiler.","keywords": ["translate", "source code", "machine code", "syntax checking", "optimization"]},
{ "question": "5. What is the importance of cybersecurity?", "keywords": ["data protection", "unauthorized access", "malware", "privacy", "security"]}]

def analyse_answer(user_answer, keywords):
    score = 0
    for keyword in keywords:
        if keyword in user_answer:
            print(f'{keyword} (1 points)')
            score += 1
    return score

    
    
names = ['Akeem Adenuga', 'Wole Soyinka', 'Fel Kuti', 'Yinka Quadri']
while True:
    fullname = input('Enter your Fullname: ')
    if fullname in names: 
        print(f'\nWelcome', fullname)
    else:
        continue


    print(f'\nInstruction: Give answers to the following questions below.')
    total_score = 0
    max_score = 0
    for question in question_bank:
        print(f'\n{question['question']}')
        user_answer = input('Enter your answer: ')
        score = analyse_answer(user_answer, question['keywords'])
        total_score += score
        max_score += len(question["keywords"])
        
        
    print(f'Total Score is {total_score} out of {max_score} ')





