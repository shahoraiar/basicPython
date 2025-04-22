fruits = ["apple", "banana", "cherry", "orange", "anaros"]

for x in fruits:
    print(x)

for x in "shahoraiar":
    print(x)

for x in fruits:
  print(x)
  if x == "banana":
    break
print('-'*20)  
for x in fruits:
   if x=='banana': continue
   print(x)

print('-'*20)  
for i in range(2,6): print(i)


print('-'*20)  
for x in range(6):
  if x == 3: break
  print(x)
else: # else not work for use break
  print("Finally finished!")

dict_data = [
   {'name':'emon', 'age': 25, 'nid': "5450133"},
   {'name':'roman', 'age': 21, 'nid': "7475896"},
   {'name':'selim', 'age': 22, 'nid': "421655"},
   {'name':'roy', 'age': 23, 'nid': "654564"},
   {'name':'banas', 'age': 16, 'nid': "824466"},
   {'name':'akbar', 'age': 17, 'nid': "256847"},
   ]

print('*'*20)
# print('data type : ', type(dict_data[0]['age']))
for x in range(len(dict_data)):
   if dict_data[x]['age']>18:
      print(dict_data[x])

# print(dict_data[0]['age'])

print('='*20)
i = 0
while i < len(dict_data): 
    print('nid : ', dict_data[i]['nid']) 
    i+=1

print('+'*20)
for x in dict_data:
   print(x['name'])

new_dict = {
   'name':'shahoraiar', 'age':10, 'nid':'3984347'
}
print(new_dict)
# print(new_dict['age'])
for key in new_dict:
   print('key : ', key)
   print(new_dict[key])