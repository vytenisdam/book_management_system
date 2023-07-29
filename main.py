# adds a new book to text file:  

def add_new_book():
    
    with open ('text.txt', 'a') as file:
        book_info = {}
        book_info['title'] = input('Insert name of the book: ').lower()
        book_info['author'] = input('Insert name of the author: ').lower()
        book_info['year'] = input('insert release date: ')
        book_info['quantity'] = input('insert how many books of the same name you would like to add: ')
        file.write(str(book_info)+'\n')

# turns text file to a dictionary and returns all info of the library:

def open_library():
        
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        for i in lines:
            print(eval(i))

# search by book name, if there are two or more books of the same title prints all of them:

def search_by_name():
           
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        choice = input('Insert your book name you would like to find: ').lower()
        rightbooks = []
        for i in lines:
            dict = eval(i)
            if dict['title'] == choice:
                rightbooks.append(dict)
            else:
                pass
        if rightbooks == []:  
            print(f"There's no such book named: {choice}. Try again.")
            search_by_name()
        else:
             for i in rightbooks:
                 print(i)  

# searches through the library by authors name. if same author has more than one book all books are given.
               
def search_by_author():
    
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        choice = input('Insert author name that you would like to find: ').lower()
        rightbooks = []
        for i in lines:
            dict = eval(i)
            if dict['author'] == choice:
                rightbooks.append(dict)
            else:
                pass
        if rightbooks == []:
            print(f'There is no author named: {choice} in the library. Try a different name.')
            search_by_author()
        else:
            for i in rightbooks:
                print(i)
            
# changes quantity of a specified:

def change_quantity():
    
    book = input('Which book: ').lower()
    quantity = input('How many: ')
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        allbooks = []
        for i in lines:
            allbooks.append(eval(i))
        for j in allbooks:
            if j['title'] == book:
                j['quantity'] = quantity
            else:
                pass
        if allbooks == []:
            print('Error. Try again.')
            change_quantity()
        else:           
            with open('text.txt', 'w') as file:
                for i in allbooks:
                    file.write(str(i) + '\n')

# deletes all info related to specified book:
                
def delete_entry():
    
    entry = input('Which book entry you want to delete: ').lower()
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        entries = []
        for i in lines:
            entries.append(eval(i))
        for j in entries:
            if j['title'] == entry:
                entries.pop(entries.index(j))
            else:
                pass
        with open('text.txt', 'w') as file:
            for i in entries:
                file.write(str(i) + '\n')

#deciding which type of search to do by author or by bookname.

def search_how():
    
    how = input("If you like to search by bookname type - 'book', or if you like to search by author name type - 'author: ").lower()
    if how == 'book':
        search_by_name()
    elif how == 'author':
        search_by_author()
    else:
        print('Something went wrong. Try again.')
        search_how()           

def book_management():
                    
    choice = input("What would you like to do with your book library:\n See all books in library type - 'see'\n Add new book type - 'add'\n Update quantity of existing book type - 'update'\n Delete existing book type - 'delete'\n Search a library for a book type - 'search': ").lower()
    if choice == 'see':
        open_library()
    elif choice == 'add':
        add_new_book()
    elif choice == 'update':
        change_quantity()
    elif choice == 'delete':
        delete_entry()
    elif choice == 'search':
        search_how()
    else:
        print('There was a mistake. Try again.')
        book_management()
        
book_management()
        
        