'''
PROBLEM :
 As a teacher, you want to analyze the grades of your students. Write a Python program that takes a list of student grades as input and provides statistics such as the average grade, minimum grade, and maximum grade.

   Guidelines:
   - Create a list that contains the grades of the students.
   - Use built-in functions such as `sum()`, `min()`, and `max()` to calculate statistics.
   - Display the average, minimum, and maximum grades to the user.
'''
def average(total_sum, length) : 
    return total_sum/length

number = input('Enter All Stuend Grade[, use for one to another number separate] : ').split(',')
new_list = []
for i in number:
    # print(type(i))
    int_number = int(i)
    new_list.append(int_number)

total_sum = sum(new_list)
print('Total SUM : ',total_sum)
minimum_number = min(new_list)
print('Minimum Number : ', minimum_number)
max_number = max(new_list)
print('Maximum Number : ', max_number)

length = len(new_list)
avg = average(total_sum, length)
print(f'Average Number: {avg:.2f}')





