# import re

# def data_analyser(file):
#     with open(file, 'r') as f:

#         for line in f.readlines():
#             pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#             matches = re.search(pattern, line)
#             if matches:
                
#                 emails = matches.group()
#                 print('AFter the group: ', emails)
#                 with open('emails.txt', 'a') as g:
#                     g.write(f"{emails}\n")
                    
    
                

                
            
        
# def data_analyser2(file):
#     phone_no = []
#     with open(file, 'r') as f:
#         for line in f.readlines():
#             pattern1 = r"\+234\s\d{3}\s\d{3}\s\d{4}"
#             matches1 = re.search(pattern1, line)
#             if matches1:
#                 phone_no = (matches1.group())
#                 with open('phone_no.txt', 'a') as g:
#                     g.write(f'{phone_no}\n')





            
import re

def data_extractor(file):
    with open(file, 'r') as f:
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        phone_pattern = r"\+234\s\d{3}\s\d{3}\s\d{4}"

        for line in f.readlines():
            email_matches = re.search(email_pattern, line)
            if email_matches:
                emails = email_matches.group()
                with open('emails.txt', 'a') as g:
                    g.write(f"{emails}\n")

            phone_matches = re.search(phone_pattern, line)
            if phone_matches:
                phone_num = phone_matches.group()
                with open('phone_no.txt', 'a') as g:
                    g.write(f"{phone_num}\n")
    
                

                
            
        


            
