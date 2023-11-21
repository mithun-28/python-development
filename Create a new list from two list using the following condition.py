# Create a new list from two list using the following condition
# Condition:  New list should contain odd numbers from the first list and even numbers from the second list.


odd_lst = []
even_lst = []

lst1 = input("Enter the elements for the list-1: ").split() 
lst2 = input("Enter the elements for the list-1: ").split()

for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
print(lst1)

for j in range(len(lst2)):
    lst2[j] = int(lst2[j])
print(lst2)

for k in range(len(lst1)):
    if lst1[k] % 2 != 0:
        odd_lst.append(lst1[k])

for l in range(len(lst2)):
    if lst2[l] % 2 == 0:
        even_lst.append(lst2[l])

print("Odd List: ",odd_lst)
print("Even List: ",even_lst)

new_lst = odd_lst + even_lst
print("Result: ",new_lst)



        

