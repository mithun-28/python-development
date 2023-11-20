# Display numbers divisible by 5 from a list

lst = input("Enter the elements of the list:").split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
    if lst[i] % 5 == 0:
        print(lst[i])
