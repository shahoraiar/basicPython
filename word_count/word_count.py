sentence = input("Enter Sentence : ",)

print('-'*60)
print("Your Sentence is : ", sentence)
print('-'*60)

separate = sentence.split()
print("Total Word : ", len(separate))
print('-'*60)

print('Total Character : ', len(sentence))
print('-'*60)

sentence_separate  = sentence.split(".")
if sentence.endswith("."):
    print('Total Sentence : ', len(sentence_separate)-1)
else:
    print('Total Sentence : ', len(sentence_separate))
print('-'*60)

