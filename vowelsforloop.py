vowels_and_constants=['a','e','i','o','u','r','t','w','A','S','D']
vowels=['a','e','i','o','u']
vowel_list=[]
constants_list=[]
for i in vowels_and_constants:
    i=i.lower()
    if i in vowels:
        vowel_list.append(i)
    else:
        constants_list.append(i)
print(vowel_list)
print(constants_list)