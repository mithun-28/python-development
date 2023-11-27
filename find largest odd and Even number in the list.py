# Python program to find largets odd and Even number in the given list

even_lst = []
odd_lst = []
lst = input("Enter the elements for the list = ").split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
print("Given list of numbers = ",*lst)

for num in lst:
    if num % 2 == 0:
        even_lst.append(num)
    else:
        odd_lst.append(num)
print("Largest even number in the given list = ",max(even_lst))
print("Largest odd number in the given list = ",max(odd_lst))

