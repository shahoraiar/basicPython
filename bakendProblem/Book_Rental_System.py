# problem : https://docs.google.com/document/d/1R1mfBpUx41DUdmwAY_8j0RqptRQqmUjw8k67ILC0fw8/edit?tab=t.0#heading=h.fanct5pcg0b1
# Assignment 1: Book Rental System (CRUD Operations + Search)

books = []

# books.append({
#     'id':1, 'title':'python_learn', 'author':'shahoraiar', 'year_published':2015, 'available':True
# })
# books.append({
#     'id':2, 'title':'new_tech', 'author':'shahoraiar', 'year_published':2020, 'available':False
# })
# books.append({
#     'id':3, 'title':'python_learn', 'author':'shahoraiar', 'year_published':2020, 'available':True
# })

def add_book():
    print('-'*5, 'ADD BOOk!!Please Fill Each Input', '-'*5)

    while True:
        try:
            id = int(input('Enter Book ID : '))
        except:
            print('[FAILED]Enter Number Only')
            continue

        for book in books:
            if book["id"] == id:
                print('[ALART]Already', id, 'Register')
                print('!!Enter Another ID please!!')
                break
        else:
            break

    title = input('Enter Book Title : ')
    author = input('Enter Book Author Name : ')
    while True:
        try:
            year_published = int(input('Enter Book Pulished Year : '))
            break
        except:
            print('[FAILED]Enter Number Only')
    while True:
            available = input('Available [True/False] : ')
            if available.lower() == 'true':
                available = True
                break
            elif available.lower() == 'false':
                available = False
                break
            else:
                print('[FAILED]Enter [True or False] Only')

    add_book_fun(id=id, title=title, author=author, year_published=year_published, available=available)

def add_book_fun(**kwargs):
    # print('id type : ', type(kwargs['id']))
    books.append(kwargs)
    print('[SUCESS]Congrats!!Book Added Successfully')

def view_books(book_ids=None):
    if len(books) <= 0 :
        print('*'*10,'No Book Available','*'*10)
        return
    print('-' * 80)
    print('SERIAL'.ljust(10), 'ID'.ljust(10), 'NAME'.ljust(20), 'AUTHOR'.ljust(20), 'YEAR'.ljust(10), 'QTY')
    print('-' * 80)

    if book_ids:
        count = 0 
        for id in book_ids:
            # print(books[id])
            for serial, book in enumerate(books):
                if serial == id : 
                    print(str(count).ljust(10), str(book['id']).ljust(10),  str(book['title']).ljust(20), str(book['author']).ljust(20), str(book['year_published']).ljust(10), book['available'])
                    count += 1
                else:
                    continue
    else : 
        for serial, book in enumerate(books):
            # print(book['id'])
            print(str(serial).ljust(10), str(book['id']).ljust(10),  str(book['title']).ljust(20), str(book['author']).ljust(20), str(book['year_published']).ljust(10), book['available'])

def update_menu():
    print('Enter 1 For EDIT BOOK NAME')
    print('Enter 2 For EDIT BOOK AUTHOR')
    print('Enter 3 For EDIT BOOK YEAR PUBLISHED')
    print('Enter 4 For EDIT BOOK AVAILABLE')

def update_book():
    view_books()

    if len(books) <= 0:
        return

    while True:
        serial = int(input('Enter The SERIAL number you want update : '))
        if len(books) <= serial :
            print('NOT VALID SERIAL NUMBER')
            continue
        break
    
    update_menu()
    while True:
        select = input('Enter [1-4] For UPDATE : ')
        if int(select) > 0 and int(select) <=4 : 
            break
        else:
            print('[INVALID]Enter ONLY [1-4] NUMBER')

    if select == '1':
        name = input('Enter UPDATE BOOK NAME : ')
        books[int(serial)]['title'] = name
        print('[SUCCESS]CONGRATS! NAME UPDATED')
    elif select == '2':
        name = input('Enter UPDATE AUTHOR NAME : ')
        books[int(serial)]['author'] = name
        print('[SUCCESS]CONGRATS! AUTHOR NAME UPDATED')
    elif select == '3':
        year = input('Enter UPDATE NAME : ')
        books[int(serial)]['year_published'] = year
        print('[SUCCESS]CONGRATS! PUBLISHED YEAR UPDATED')
    elif select == '4':
        while True:
            available = input('Enter UPDATE AVAILABLE [True/False] : ')
            if available.lower() == 'true':
                books[int(serial)]['available'] = True
                print('[SUCCESS]CONGRATS! AVAILABLE UPDATED')
                break
            elif available.lower() == 'false':
                books[int(serial)]['available'] = False
                print('[SUCCESS]CONGRATS! AVAILABLE UPDATED')
                break
            else:
                print('[FAILED]Enter [True or False] Only')
         
    

def delete_book():
    view_books()
    if len(books) <= 0:
        return
    while True:
        serial = int(input('Enter The SERIAL number you want update : '))
        if len(books) <= serial :
            print('[INVALID]NOT VALID SERIAL NUMBER')
            continue
        break
    books.pop(serial)
    print('[SUCCESS]CONGRATS! DELETE THE BOOK')

def search_book():
    if len(books) <= 0:
        print('*'*10,'No Book Available','*'*10)
        return
    
    search = input('INPUT YOUR SEARCH :')
    count = 0
    match_ids = []
    for book in books:
        count += 1
        lower_title = str(book['title']).lower()
        lower_author = str(book['author']).lower()
        # print('lower : ', lower_title)

        upper_title = str(book['title']).upper()
        upper_author = str(book['author']).upper()
        # print('upper :', upper_title)

        if lower_title.startswith(search) or lower_author.startswith(search):
            match_ids.append(count-1)
        elif upper_title.startswith(search) or upper_author.startswith(search):
            match_ids.append(count-1)
        

    # print('ids ', match_ids)
    if len(match_ids) > 0:
        view_books(match_ids)
    else:
        print('-'*5,'SERACH BOOK IS NOT AVAILABLE','-'*5)

def menu():
    print('-'*5, 'Select Menu', '-'*5)
    print('Enter 1 For ADD BOOK')
    print('Enter 2 For SHOW BOOK')
    print('Enter 3 For UPDATE BOOK')
    print('Enter 4 For DELETE BOOK')
    print('Enter 5 For SEARCH BOOK')
    print('Enter 6 For Exit')

while(True):
    menu()
    select = input('Please Enter : ')
    if select == "1":
        add_book()
    elif select == '2':
        view_books()
    elif select == '3':
        update_book()
    elif select == '4':
        delete_book()
    elif select == '5':
        search_book()
    elif select == "6":
        print('Thank You! \n!!Come AGAIN!!')
        break
    else:
        print('[FAILED]Enter ONLY [1-3]')



