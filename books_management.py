import csv 

column_names = ['title', 'author', 'year', 'quantity']

# used this to create csv file
# books = [{
#          'title': 'Lord of the rings',
#          'author': 'J.R.R. Tolkien',
#          'year': 1932,
#          'quantity': 1
#            }]

# # creating a header:
def create_header():
    
    with open ('library.csv', 'w', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = column_names)
        writer.writeheader() 
        #writer.writerows(books)



#appending a book to existing file:
def add_new_book():
    
    with open('library.csv', 'a', newline = '') as object:
        book_info = {}
        book_info['title'] = input('Insert name of the book: ')
        book_info['author'] = input('Insert name of the author: ')
        book_info['year'] = input('insert release date: ')
        book_info['quantity'] = input('insert how many books of the same name you would like to add: ')
        write_object = csv.DictWriter(object, fieldnames = column_names)
        write_object.writerow(book_info)

#opens existing book library:
def open_library():   
     
    with open('library.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

#add_new_book()        
# deleting a selected book from a library(how?):

#with open('library.csv', 'r') as csvfile:
#    pass

# Search by bookname:
def search_by_book():
    
    with open('library.csv', 'r') as csvfile:
        name = input('insert the name of the book you like: ')
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == name:
                print(row)
                
# Search by author:
def search_by_author():
    
    with open('library.csv', 'r') as csvfile:
        name = input('insert the name of the author you like: ')
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] == name:
                print(row)
                
# Updating quantity of the selected book( doesnt work):

def updating_quantity():
    
    with open('library.csv', 'r') as csvfile:
        name = input('insert the name of the book you like: ')
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == name:
                with open('library.csv', 'a', newline = '') as file:
                    csv.DictWriter(file, fieldnames = column_names)
                    row[3] += input('new num: ')
add_new_book()
# updating_quantity()
open_library()




