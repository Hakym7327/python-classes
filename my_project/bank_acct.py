import re
import hashlib
import sqlite3
import random
import time


from getpass import getpass

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number INTEGER NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    account_balance ₦ INTEGER NOT NULL
    )
""")


def first_page():

    menu = """
        *************************NICO BANK*******************************
        Welcome to Nico Bank Mobile Banking. 
        1. Create Account
        2. Log In
        """
        
    while True:
            print(menu)
            choice = input("Choose an option from the menu above: ").strip()
            if choice == "1":
                Create_account()
            elif choice == "2":
                log_in()
            else:
                print("Invalid choice")
                continue

def Create_account():
    while True:
        
        first_name = input("Enter your firstname: ").strip().title()
        pattern = r'^[A-Za-z]+$'
        match = re.search(pattern, first_name)
        if not match:
            print("Invalid name! Use only letters and spaces (4-255 characters).")
            continue
        
        last_name = input("Enter your lastname: ").strip().title()
        pattern = r'^[A-Za-z]+$'
        match = re.search(pattern, last_name)
        if not match:
            print("Invalid name! Use only letters and spaces (4-255 characters).")
            continue

        full_name = first_name + " " + last_name
        
        break
     
        
    while True:
        username = input(f'Enter a username {full_name}: ').strip()
          
        pattern = r"^[A-Za-z0-9_]{3,20}$"
        match = re.search(pattern, username)
        if not match:
            print("Invalid input. Make sure it's 3-20 characters and uses only letters, numbers, or underscores.")
            continue
        break


    while True:
        email = input("Enter your email address: ").strip()
        if not email:
            print("Email field cannot be blank")
            continue

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        match = re.match(pattern, email)
        if not match:
            print("Email address is invalid")
            continue
        break

    while True:
        password = getpass("Enter your password: ").strip()
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,30}$'
        match = re.match(pattern, password)
        if not match:
            print('Your password must have atleast one uppercase letter, one lowercase letter, one number, one special case character and minimum of 8 characters')
            continue
        

        while True:
            confirm_password = getpass("Confirm your password: ").strip()
            if not confirm_password:
                print("Confirm Password field cannot be blank")
                continue

            if password != confirm_password:
                print("Passwords dont match")
                continue
            break
        break

    hashed_password = hashlib.sha256(password.encode()).hexdigest()



    while True:
        try:
            account_balance = float(input('Enter your initial deposit: '))
            # formatted_amount = f"₦{account_balance}"

            if not account_balance:
                print('Initial deposit cannot be blank')
                continue

            if account_balance < 2000:
                print("You need to deposit at least 2000 to open an account.")
                continue
            
            if account_balance < 0:
                print("Negative numbers are not allowed, TRY AGAIN>")
                continue
            break
            
            
        except ValueError:
            print('Input a valid deposit')
        
        
            
    while True:
        account_number = random.randint(2040000000, 9099999911)
        useable = cursor.execute("SELECT id  FROM accounts WHERE account_number = ?", (account_number,)).fetchone()
        if useable is None:
            break
        continue            
            



    try:
        cursor.execute("INSERT INTO accounts (account_number, full_name, username, email, password, account_balance) VALUES(?, ?, ?, ?, ?, ?)", (account_number, full_name, username, email, hashed_password, account_balance))
    except sqlite3.IntegrityError as e:
        print('Intergrity Error: ', e)
    else:
        print("Loading", end="")
        for _ in range(4):
            time.sleep(1)
            print(".", end="", flush=True)
        print("\nAccount created successfully 😁")
        print(f"This is your New Account number: {account_number}\nAvailable balance: ₦{account_balance}")
        conn.commit()
        log_in()
        
def log_in():
   
    print("""
         \n  **********************Nico bank***************************  
         \n*************************LOG IN*******************************
           """)
    i = 3
    while i > 0:      
        username = input('Enter your username: ').strip()
        password = getpass('Enter your password: ').strip()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = cursor.execute(" SELECT id, full_name, username, account_number, email FROM accounts WHERE username = ? AND password = ?", (username, hashed_password)).fetchone()
        if user is not None:
            print("Loading", end="")
            for _ in range(4):
                time.sleep(1)
                print(".", end="", flush=True)
            print('\nLog in Sucessful 😊')
            bank_menu(user)
            
        elif user is None:
            print(f'Incorrect Credentials. you have {i - 1} tries left')
            i -= 1
            continue    
    else:
        print('Maximum tries exceeded, try again later')

def bank_menu(user):
    id, full_name, username, account_number, email = user
    print(f"\nWelcome, {full_name}")
    
    menu = """
    ********************Nico Bank******************
    1. Deposit.
    2. Balance Inquiry.
    3. Withdrawal.
    4. Transfer to other Bank Accounts.
    5. Transaction History.
    6. Account Details.
    7. Log Out
    """    

    while True:
        print(menu)
        choice = input("Choose an option from the options above: ").strip()
        if choice == "1":
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            deposit(user)

        elif choice == "2":
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            balance(user)
            

        elif choice == "3":
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            withdrawal(user)

        elif choice == "4":
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            transfer(user)

        elif choice == "5":
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            transaction(user)

        elif choice == "6":
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            account_details(user)

        elif choice == "7":
            choice = input("\nAre you sure you wanna log out Yes/No: ").strip().lower()
            if choice == 'yes': 
                print("Loading", end="")
                for _ in range(3):
                    time.sleep(0.5)
                    print(".", end="", flush=True)
                print("Good bye 👋")
                first_page()
            elif choice == 'no':
                print("Loading", end="")
                for _ in range(3):
                    time.sleep(0.3)
                    print(".", end="", flush=True)
                continue
        
        else:
             print("Invalid choice.")
             continue   

def deposit(user):
    id, full_name, username, account_number, email = user
    user_info = cursor.execute(" SELECT id, account_balance FROM accounts WHERE account_number = ?", (account_number,)).fetchone()
    id, account_balance = user_info
    while True:
        try:
            deposit_amount = float(input("\nEnter deposit amount: "))
            if not deposit_amount:
                print("You have to input an amount.")
                continue
            
            elif deposit_amount <= 0:
                print('Your deposit cant be negative number or zero!!!!')
                continue
            break
        except ValueError as e:
            print(f"{e}, you need to input a valid amount!!")
            continue
        except Exception:
            print("Invalid input!!!")
            continue
    
    account_balance += deposit_amount
    print("Loading", end="")
    for _ in range(4):
        time.sleep(1)
        print(".", end="", flush=True)
    print(f"\nDeposit Sucessful\nYour New Balance is: ₦{account_balance}")
    cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_number = ?", (account_balance, account_number))
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number INTEGER,
        full_name TEXT,
        transaction_type TEXT,
        amount INTEGER,
        account_balance ₦
        )
    """)
    cursor.execute("INSERT INTO transactions (account_number, full_name, transaction_type, amount, account_balance) VALUES(?, ?, ?, ?, ?)", (account_number, full_name, "Deposit", deposit_amount, account_balance))
    conn.commit()
    
def balance(user):
    id, full_name, username, account_number, email = user
    user_info = cursor.execute(" SELECT id, account_balance FROM accounts WHERE account_number = ?", (account_number,)).fetchone()
    id, account_balance = user_info
    print(f'\n{full_name}, your account balance is ₦{account_balance}.')   
    
def withdrawal(user):

        id, full_name, username, account_number, email = user
        user_info = cursor.execute(" SELECT id, account_balance FROM accounts WHERE account_number = ?", (account_number,)).fetchone()
        id, account_balance = user_info
        while True:
            try:
                withdrawal_amount = int(input(f"\nEnter withdrawal amount {full_name}: "))
                
                if withdrawal_amount <= 0:
                    print('Withdrawal amount must be a positive valid number and cannot be zero!!!')
                    continue
                if withdrawal_amount > account_balance:
                    print("Insufficient Funds!!!!!")
                    continue
                break

            except ValueError as e:
                print(f"{e}, Withdrawal amount must be a number!!!!")
                continue
            except Exception as e:
                print(f"{e}, Invalid Input")
                continue

        account_balance -= withdrawal_amount
        print("Loading", end="")
        for _ in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
        print(f"\n\nYour withdrawal of ₦{withdrawal_amount} is succesfull.\nYour available balance is: ₦{account_balance}.")

        cursor.execute("UPDATE accounts SET account_balance = ? WHERE full_name = ?", (account_balance, full_name))
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER,
            full_name TEXT,
            transaction_type TEXT,
            amount INTEGER,
            account_balance ₦
            )
          """)
        cursor.execute("INSERT INTO transactions (account_number, full_name, transaction_type, amount, account_balance) VALUES(?, ?, ?, ?, ?)", (account_number, full_name, "Withdrawal", withdrawal_amount, account_balance))
        conn.commit()
        redo = input("\nDo you want to make another withdrawal Yes/No: ").strip().lower()
        if redo == 'yes':
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            withdrawal(user)
        elif redo == 'no':
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            bank_menu(user)
        else:
            print("Invalid Input")
    
def transfer(user):

    id, full_name, username, account_number, email = user
    user_info = cursor.execute(" SELECT id, account_balance FROM accounts WHERE account_number = ?", (account_number,)).fetchone()
    id, account_balance = user_info
    while True:
        try:
            recipient_account = int(input("\nEnter recipient account number: "))
            recipient_info = cursor.execute(" SELECT id, full_name, account_balance FROM accounts WHERE account_number = ?", (recipient_account,)).fetchone()
            if len(str(recipient_account)) < 10:
                print("Invalid!, account number must be 10 digits!!")
                continue
            if recipient_account == account_number:
                print("You cannot send transfer to self!!")
                continue
            if recipient_info is None:
                print("\nRecipient cannot be found!!")
                continue
            recipient_id, recipient_name, recipient_balance = recipient_info
            print("Loading", end="")
            for _ in range(3):
                time.sleep(0.2)
                print(".", end="", flush=True)
            print(f"\n\nRecipient found.\nFull_name: {recipient_name}")

        except ValueError as e:
            print("Invalid Input!", e)    
            continue

        except Exception as e:
            print("Invalid Input!", e) 
            continue   

        while True:
            try:
                transfer_amount = int(input("\nEnter transfer amount: "))
                if transfer_amount <= 0:
                    print("Amount has to be a positive number!")
                    continue
                if transfer_amount > account_balance:
                    print("Insufficient funds!!")
                    continue
                break
            except Exception as e :
                print("Invalid input", e)
                continue

        

        account_balance -= transfer_amount
        recipient_balance += transfer_amount
        print("Loading", end="")
        for _ in range(4):
            time.sleep(1)
            print(".", end="", flush=True)
        print(f"\n\nTransfer Sucessfull\nAmount: ₦{transfer_amount}\nAvailable balance: ₦{account_balance} ")
        break

    cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_number = ?", (account_balance, account_number))
    cursor.execute("UPDATE accounts SET account_balance = ? WHERE account_number = ?", (recipient_balance, recipient_account))
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number INTEGER,
        full_name TEXT,
        transaction_type TEXT,
        amount INTEGER,
        account_balance ₦
        )
    """)
    cursor.execute("INSERT INTO transactions (account_number, full_name, transaction_type, amount, account_balance) VALUES(?, ?, ?, ?, ?)", (account_number, full_name, "Debit", transfer_amount, account_balance))
    cursor.execute("INSERT INTO transactions (account_number, full_name, transaction_type, amount, account_balance) VALUES(?, ?, ?, ?, ?)", (recipient_account, recipient_name, "Credit", transfer_amount, recipient_balance))
    conn.commit()
      
def transaction(user):


    id, full_name, username, account_number, email = user
    transactions = cursor.execute(" SELECT transaction_type, amount, account_balance FROM transactions WHERE account_number = ?", (account_number,)).fetchall()
    if transactions is None:
        print("\nThere is no transaction history")
    for transaction in transactions:
        transaction_type, amount, available_balance = transaction
        print(f"\nTransaction type: '{transaction_type}' | Amount: ₦{amount} | Available_balance: ₦{available_balance}")
        
def account_details(user):
      id, full_name, username, account_number, email = user
      print(f"\nFullname: {full_name} | Account number: {account_number} | Username: {username} | Email: {email}")
      
      
       
   

while True:
     




    first_page()
   
    
            

            


            
            
            
                
        
            
     
            
        

               




