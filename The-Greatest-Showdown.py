#Task 1: Identify the Greatest

print("Enter 3 numbers one at a time as asked")

num_one = input("Enter the first number: ")
num_two = input("Enter the second number: ")
num_three = input("Enter the third number: ")

if (num_one >= num_two) and (num_one >= num_three):
    largest = num_one
elif(num_two >= num_one) and (num_two >= num_three):
    largest = num_two
else:
    largest = num_three

#Task 2: Identify the Smallest
if (num_one <= num_two) and (num_one <=num_three):
    smallest = num_one
elif(num_two <=num_one) and (num_two <= num_three):
    smallest = num_two
else:
    smallest = num_three

#Below are my print statements for each scenario
if largest == num_one:
    print("The first number " + largest + " is the largest number")
elif largest == num_two:
    print("The second number " + largest + " is the largest number")
else:
    print("The third number " + largest + " is the largest number")

if smallest == num_one:
    print("The first number " + smallest + " is the smallest number")
elif smallest == num_two:
    print("The second number " + smallest + " is the smallest number")
else:
    print("The third number " + smallest + " is the smallest number")
