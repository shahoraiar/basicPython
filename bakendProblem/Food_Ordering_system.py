foods = {'Chicken Roast': 90, 'Shami Kabab':25, 'Mutton Curry': 110, 'Beef Bhuna': 90, 'Ruhi Fish': 80, 'Vegetable Bhaji': 40, 'Plain Dal': 40, 'Potato Bharta': 20, 'Hilsha Shorshe': 180, 'Firni': 25, 'Beef Tehari': 140, 'Plain Rice': 15}
order_list = []


def food_menu():
    print('WELCOME TO FOOD MENU'.center(50, '*'))
    print('SERIAL'.center(15), 'FOOD NAME'.center(25), 'PRICE'.center(10))
    for i, (name, price) in enumerate(foods.items(), start=1):
        print(str(i).rjust(3, "0").center(15), name.center(25, '-'), str(price).center(10))

def place_order():
    food_menu()
    food_set = set()
    serial = input('ENTER THE SERIAL NUMBER FOR ORDER FOOD [use , for separate order from one to another]: ').strip().replace(',', '')
    # print('serial : ', serial)         
    # print('serial type: ', type(serial))   
    # print('split : ', serial.split(' '))
    for i in serial.split(' '):
        while not i.isdigit():
            print('[INVALID] INTER THE CORRECT SERIAL : ', i)
            break
        else:
            food_set.add(int(i))  
    
    print(food_set)

def show_menu():
    print('-'*8, 'MENU', '-'*8)
    print('ENTER 1 FOR SHOW FOOD MENU')
    print('ENTER 2 FOR ORDER FOOD')
    print('ENTER 3 FOR VIEW ORDER FOOD')
    print('ENTER 4 FOR CANCEL ORDER FOOD')
    print('ENTER 5 FOR GENERATE')
    print('ENTER 6 FOR EXIT')
    print(('ENJOY THE FOOD').center(30, '*'))

while(True):
    show_menu()
    select = input('[INPUT]ENTER YOUR VALUE : ')
    match select:
        case '1':
            food_menu()
        case '2':
            place_order()
        case '3':
            ...
        case '4':
            ...
        case '5':
            ...
        case '6':
            exit()
        case _:
            print('[INVALID] PLEASE INPUT [1-6]')

