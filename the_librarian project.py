# library = [
#     {"title": "Things Fall Apart", "author": "Chinua Achebe", "year_published": 1958, "isbn": "7867-678-546-532", "available": True},
#     {"title": "Half Of A Yellow Sun", "author": "Chimamanda Ngozi Adichie", "year_published": 2006, "isbn": "6797-742-641-894", "available": True},
#     {"title": "Purple Hibiscus", "author": "Chimamanda Ngozi Adichie", "year_published": 2003, "isbn": "6767-424-524-782", "available": True},
#     {"title": "The Famished Road", "author": "Ben Okri", "year_published": 1991, "isbn": "7543-218-430-218", "available": True},
#     {"title": "The Death of Vivek Oji", "author": "Akwaeke Emezi", "year_published": 2020, "isbn": "3329-741-997-437", "available": True},
# ]



library = [{"title": "Half Of A Yellow Sun", "author": "Chimamanda Ngozi Adichie", "year_published": 2006, "isbn": "1234-567-891-234", "available": True}]


def add_book():
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author: ").strip()
    year_published = input("Enter the year published: ").strip()
    isbn = input("Enter the ISBN: ").strip()

    print('Before: ', library)
    library.append({"title": title, "author": author, "year_publiched": year_published, "isbn": isbn, "available": True})

    print('After: ', library)
    return f"Book '{title}' by {author} has been added to the library successfully"




def view_books():
    print('\n')
    print(library)


def update_books(isbn):
    print('The number of books you have is: ', len(library))
    
    for book in library:
        print('\n')
        print('Each book: ', book)


        
        if book['isbn'] == isbn:

           
            option = input('What information of the book do you want to update: title, author, year_published, isbn: ')

            while option not in ['title', 'author', 'year_published', 'isbn']:
                option = input('Invalid selection... What information of the book do you want to update: title, author, year_published, isbn: ')

            if option == 'title':
                book['title'] = input('Enter an updated title for your book: ')
                print('\n')
                print(book)
                print('Book has been Updated Sucessfully')
            elif option == 'author':
                book['author'] = input('Enter an updated author for your book: ')
                print('\n')
                print(book)
                print('Book has been Updated Sucessfully')
            elif option == 'year_published':
                book['year_published'] = input('Enter an updated year for your book: ')
                print('\n')
                print(book)
                print('Book has been Updated Sucessfully')
            elif option == 'isbn':
                book['isbn'] = input('Enter an updated isbn for your book: ')
                print('\n')
                print(book)
                print('Book has been Updated Sucessfully')
            # else:
            #     print('\n')
            #     continue


def delete_book(isbn):
    for book in library:
        if book['isbn'] == isbn:
            del book
        print(f'\n Book with isbn {isbn} has been sucessfully removed')


def search_book(title):
    for book in library:
        if book['title'] == title:
            print(f'\n Book found \n title: {book["title"]}, author: {book['author']}, year_published: {book['year_published']}, isbn: {book['isbn']}, availability: {book['available']}')


def borrow_book(isbn):
    for book in library:
        if book['isbn'] == isbn:
            if book['available'] == True:
                book['available'] = False
                print(f'\n{book['title']} has been sucessfully borrowed to you, kindly return on specified date')
            else:
                print('Book has already been borrowed, kindly go for other books')


def return_book(isbn):
    for book in library:
        if book['isbn'] == isbn:
            book['available'] = True
            print(f'\n{book['title']} has been Returned and available for Borrowing')



      
        
            
    




            



menu = """
***********************MENU*****************************
1. Add Book
2. View Book
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Exit
"""

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ")
    if choice == "1":
        print(add_book())
    elif choice == "2":
        view_books()
    elif choice == "3":
        isbn = input('Enter isbn: ')
        update_books(isbn)
    elif choice == "4":
        isbn = input('Enter isbn: ')
        delete_book(isbn)
    elif choice == "5":
        title = input('Enter title: ').title()
        search_book(title)
    elif choice == "6":
        isbn = input('Enter isbn of the book you want to borrow: ')
        borrow_book(isbn)
    elif choice == "7":
        isbn = input('Enter isbn of the book you want to return: ')
        return_book(isbn)
    elif choice == "8":
        print("Exiting the library...")
        break
    else:
        print("Invalid choice")
        continue
