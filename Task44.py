user_name=input("please enter your name:")
vowel=['a', 'e','i','o', 'u']
vowel_count=0
counter=0
while counter < len(user_name):
    if user_name[counter].lower() in vowel:
        vowel_count +=1
        counter += 1
        print("vowel_count")