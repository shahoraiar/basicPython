a = int(input('Enter first Number : '))
b = int(input('Enter second Number : '))
c = int(input('Enter third Number : '))

if a==b and b==c:
    print(f"{a}, {b}, {c} are equal")

elif a==b or b==c or c==a:
    print('Two numbers are equal! Cannot compare middle. Please try again.')

elif (b<=a and a<=c) or (b>=a and a>=c): # b<a< c or b>a> c
    print(a, 'a is Middle number')

elif (a<=b and b<=c) or (a>=b and b>=c): # a<b< c or a>b>c
    print('Middle number is b : ', b)

else: #elif (a<=c and c<=b) or (a>=c and c>=b): # a<c<b or a>c>b
    print(f'Middle {c} number c')

