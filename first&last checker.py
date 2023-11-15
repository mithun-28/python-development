# Check if the first and last number of a list is the same

lst = input("Enter the list elements: ").split()
for i in range (len(lst)):
    lst[i] = int(lst[i])
if(lst[0] == lst[-1]):
    print("First and last element of the list are same.")
else:
    print("First and last element of the list are not same.")
