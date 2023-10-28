num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))

# make sure num1 is smaller than num2
if num1>num2:
    num1,num2 = num2, num2
sum_of_numbers=0   #initialize the sum to 0
# iterate through the numbers between num1 and num2(inclusive)
for current_num in range(num1,num2 + 1):
    sum_of_numbers += current_num  #add the current number to the sum
print("The sum of number between", num1, "and", num2, "is", sum_of_numbers)
