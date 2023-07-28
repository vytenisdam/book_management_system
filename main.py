# adds a new book to text file:  

def add_new_book():
    
    with open ('text.txt', 'a') as file:
        book_info = {}
        book_info['title'] = input('Insert name of the book: ')
        book_info['author'] = input('Insert name of the author: ')
        book_info['year'] = input('insert release date: ')
        book_info['quantity'] = input('insert how many books of the same name you would like to add: ')
        file.write(str(book_info)+'\n')

# turns text file to a dictionary and returns all info of the library:

def open_library():
        
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        for i in lines:
            print(eval(i))

# search by book name:

def search_by_name():
           
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        choice = input('Insert your book name you would like to find: ')
        for i in lines:
            dict = eval(i)
            if dict['title'] == choice:
                print(dict)
            else: 
                pass   

# search by author:

def search_by_author():
    
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        choice = input('Insert author name you would like to find: ')
        for i in lines:
            dict = eval(i)
            if dict['author'] == choice:
                print(dict)
            else: 
                pass
            
# changes quantity of a specified:

def change_quantity():
    
    book = input('Which book: ')
    quantity = input('How many: ')
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        allbooks = []
        for i in lines:
            allbooks.append(eval(i))
        for j in allbooks:
            if j['title'] == book:
                j['quantity'] = quantity
        with open('text.txt', 'w') as file:
            for i in allbooks:
                file.write(str(i) + '\n')

# deletes all info related to specified book:
                
def delete_entry():
    
    entry = input('Which book entry you want to delete: ')
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        entries = []
        for i in lines:
            entries.append(eval(i))
        for j in entries:
            if j['title'] == entry:
                entries.pop(entries.index(j))
        with open('text.txt', 'w') as file:
            for i in entries:
                file.write(str(i) + '\n')
