# Program to find whether the given element is present in the list

def element_finder(lst,search):
    if search in lst:
        return True
    else:
        return False
        

lst = [] # Create an empty list
size = int(input("Enter the size of the list: "))
for i in range(size):
    ele = int(input("Enter the element: "))
    lst.append(ele)
search = int(input("Enter the element to be checked: "))
if element_finder(lst,search) == True:
    print(search," is present in the list at the index position ",i)
else:
    print(search," is not present in the list!")

