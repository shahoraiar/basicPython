def is_palindrom(word) -> bool : 
    # if word[:] == word[::-1]:
    #     return True
    # else:
    #     return False
    for i in range(len(word)//2) : 
        print(i)
        if word[i] == word[len(word)-i-1] : 
            print('first : ', word[i])
            print('last : ',word[len(word)-i-1])
            continue
        else : 
            return False
    else:
        return True

word = input('enter word : ')
print(is_palindrom(word))
