# Python program to find max of two numbers and to find the total of the two numbers

def max_num(num1,num2):
    if num1 > num2:
        print(num1,"is greater than",num2)
    else:
        print(num2,"is greater than",num1)
def sum_num(num1,num2):
    tot = num1 + num2
    print("Sum of the given two numbers:",tot)


num1 = int(input("Enter the number: "))
num2 = int(input("Enter another number: "))

max_num(num1,num2)
sum_num(num1,num2)

