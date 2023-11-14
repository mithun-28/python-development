# Program to find factorial of the number

num = int(input("Enter the number: "))
fact = 1

while num > 1:
    fact *= num
    num -= 1
print(fact)
