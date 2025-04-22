'''
Problem : 
 You want to create a simple task tracker to keep track of your daily tasks. Write a Python program that allows you to add tasks to a list, mark tasks as completed, and display the list of tasks.
   Guidelines:
   - Create an empty list to store the tasks.
   - Implement a menu system that allows the user to add tasks, mark tasks as completed, and display the list of tasks.
   - Use appropriate input statements to interact with the user and modify the list accordingly.
   - Ensure that the program continues running until the user chooses to exit.
'''

tasks = []
def show_menu():
    print('--------Menu start--------' )
    print('Enter 1 For ADD Task')
    print('Enter 2 For Show Task  ')
    print('Enter 3 For Mark Task As Complete')
    print('Enter 4 For Exit')
    print('--------Menu End--------' )

def add_task():
    enter_task = input("[INPUT] Enter Task Name : "  )
    for i in tasks:
        if enter_task ==  i['task']:
            print('[WARNING]',enter_task, 'name already exists')
            break
    else:
        tasks.append({'task': enter_task, 'complete': False})
        print('[SUCCESS]!!!!!!!Task Added Succesfully!!!!!!!')

def show_task():
    if len(tasks) <= 0:
        print('[SUCCESS] Empty Task')
    else:
        for i in tasks:
            print('[SUCCESS] task name : ', i["task"], ' || complete : ', i['complete'])

def mark_complete():
    show_task()
    name = input('[INPUT] Enter Task Name For Complete : ')
    for i in tasks :
        if name == i['task'] and i['complete'] == True:
            print('[WARNING] Already Task [', name, '] Completed')
            break
        elif name == i['task']:
            i['complete'] = True
            print('[SUCCESS]', name, 'Task Completed')
            break
    else: 
        print('[WARNING]', name, 'not found in the task list')

while True : 
    show_menu()
    select = input('Select Menu Enter 1-4 : ')

    if select == "1": 
        add_task()
    elif select == "2":
        show_task()
    elif select == "3":
        mark_complete()
    elif select == "4":
        print('[SUCCESS] Exit!! From The Task! Good Bye ! Come Again !!')
        break
    else:
        print('[WARNING] Enter only [1-4] Number : ')