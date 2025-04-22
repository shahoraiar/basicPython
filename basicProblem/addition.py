# sum = 0
# my_var = []
# for x in range(101):
#     # if x % 2 == 0:
#     #     # print(x)
#     #     sum = sum + x
#     if x % 5 == 0:
#         my_var.append(x)
#         # continue
        

#     sum = sum + x

#     print(x)
#     x =- 1

# print('sum : ', sum)

# sum = 0
# for x in range(11):
#     if x % 2 == 0:
#         print(x)
#         sum = sum + x

# print('sum : ', sum)

# x = 100
# sum = 0
# while x > -1:
#     # print(x)
#     if x % 2 != 0:
#         sum = sum+x
#     if x % 5 == 0 :
#         print(x) 
#         x -= 1
#         continue
#     x -= 1
# print('odd sum : ', sum)
# for x in range(100,-1,-1):
#     print(x)


# my_var = []
# for x in range(101):
#     if x % 5 == 0:
#         my_var.append(x)
#         # continue
        
#     print(x)
#     x =- 1

# print('my list ', my_var)

numbers = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

input_num = int(input('enter number : '))
if input_num in numbers : 
    print('the number is already exists!')
else : 
    numbers.append(input_num)
    print(numbers)

# flag = 0
# for x in numbers:
#     if input_num in numbers:
#         print('yes number already exists!')
#         # flag = 1
#         break
# # if flag == 0:
#     numbers.append(input_num)
    # print(numbers)

