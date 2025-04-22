num_1 = int(input('Enter first Number : '))
num_2 = int(input('Enter second Number : '))
num_3 = int(input('Enter third Number : '))

if num_1 == num_2 and num_2==num_3:
    print(f"{num_1}, {num_2}, {num_3} are equal")

elif num_1 >= num_2 and num_1 >= num_3:
    print(num_1, 'num_1 is biggest number')

elif num_1 <= num_2 and num_3 <= num_2:
    print('biggest number is num_2 : ', num_2)

elif num_1 <= num_3 and num_2 <= num_3:
    print(f'biggest {num_3} number num_3')

maximum = max(num_1, num_2, num_3)
print('The biggest number using function : ', maximum)