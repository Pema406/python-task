user_name = input("Enter your name:")
contain_vowel=False
vowels = "aeiou"
for char in user_name:
    if char.lower() in vowels:
        contains_vowel =True
        break
    print("has_vowel")