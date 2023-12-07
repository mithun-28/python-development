# Removing duplicates from the list

lst = input("Enter the elements for the list: ").split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
print("Orginal List = ",lst)

result_lst = set(lst)
print("List without Duplicates = ",list(result_lst))
