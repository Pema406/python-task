user_name= input("Enter your names:")
contains_vowel=False
vowels = "aeiou"
index = 0
while index <len(user_name):
    if user_name[index].lower() in vowels:
        contains_vowel = True
        break
    index +=1

