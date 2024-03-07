# A lambda function is a small anonymous function.
# syntext , lambda arguments : expressio

# example 1 : 
x = lambda a : a + 10
print('example-1 : ',x(10)) #20

# example 2 : 
x = lambda a , b : a * b
print('example-2 : ',x(5,5))

# example 3 : 
def myfunc(n) : 
    return lambda a : n + n + a

myDoubler = myfunc(10) # myDoubler now holds a function that adds 10 + 10 + a, where a is an argument || myDoubler itself is not a function, but it holds a reference to a function (specifically, a lambda function returned by myfunc)

final = myDoubler(2) # Calling myDoubler with argument 2, which results in 10 + 10 + 2 = 22 || use myDoubler(2), you're effectively using myDoubler as a function because it references a function
print('example-3 : ',final)


# example 4 : Lambda Function with filter()
# The filter() method accepts two arguments in Python: a function and an iterable such as a list.
list1 = [10,25,51,15,60,33]
odd_list = list(filter(lambda x : (x%2 != 0) , list1))

print('exercise-4 : ',odd_list)

