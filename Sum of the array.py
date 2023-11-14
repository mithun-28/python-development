# Program to find sum of the array

array = []
size = int(input("Enter the size of the array: "))

for i in range (size):
    ele = int(input("Enter the elements: "))
    array.append(ele)
print("Your array = ",array)
sum = 0
for i in range (size):
    sum += array[i]
print("Sum of the array elements = ",sum)
