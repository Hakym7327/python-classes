# 15/4/25
# book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
book_info = "george orwell ; 1984 ; 1949 ; ISN 978-0-452-28423-4 ; 328 ; 1999"
book_info = book_info.split(" ; ")
author, book_title, year_published, isbn, no_of_pages, cost = book_info
# author = book_info[0]
# book_title = book_info[1]
# year_Published = book_info[2]
# isbn = book_info[3]
# no_of_pages = book_info[4]
# cost = book_info[5]
# num = 9.56755

# print("{0:.3f}".format(num))

# # print("author", author)
# # print("book_title", book_title)
# print("year_Published", year_published)
# print("isbn", isbn)
# print("no_of_pages", no_of_pages)
# print("cost", cost)

author = author.title()
book_title = str(book_title.strip() .title())
isbn = isbn.replace('ISN','ISBN')
cost = "₦{0:.2f}".format(float(cost))

formatted_book_info = f' The book {book_title} was written by {author} and published in {year_published}.\n It has {no_of_pages} pages and {isbn} and costs {cost}.'
# formatted_book_info = 'The book {} was written by {} and published in {}.\nIt has {} pages and {} and cost {}.'.format(book_title,author,year_published,no_of_pages,isbn,cost)              
print(formatted_book_info)


