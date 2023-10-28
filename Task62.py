user_input =[]
for i in range(3):
    number = int(input("enter a number:"))
    print(user_input)
def is_even(user_input):
    for number in user_input:
        if number % 2 !=0:
            return False
            return True