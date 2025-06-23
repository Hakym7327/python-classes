import sqlite3
# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('students.db')

# # Create a cursor object
cursor = conn.cursor()

# # Create a table called students
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender CHAR(1) NOT NULL check (gender in ('M', 'F'))
);
''')

# cursor.execute('''
# INSERT INTO students(name, age, gender)
#                VALUES('Tobi Dada', '72', 'M'),
#                      ('Nico Dada', '98', 'M');
#                      ()

# ''')


# cursor.execute('''
# INSERT INTO students(name, age, gender)
#                VALUES('Tobi Dada', '72', 'M');

# ''')
# conn.commit()

cursor.execute('''SELECT * 
                  FROM students
                  WHERE id = 6;
               ''')

rows = cursor.fetchone()

print(rows)
# for row in rows:
#     print(row)
