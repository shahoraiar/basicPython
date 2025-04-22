x = 7
print('x id : ', id(x))
# y = x
# print('y id : ', id(y))
x = 9 
print('x new id : ', id(x))
x = 7 
print('same x 7 id : ', id(x))

a = [4, 5, 6]
print('a  id : ', id(a))
a[0] = 7
print('a new id : ', id(a))
a[0] = 4
print('a again  id : ', id(a))

