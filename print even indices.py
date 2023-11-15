#  Print characters from a string that are present at an even index number

string = input("Enter a string: ")
print("The even indices cahracters")
for i in range(len(string)):
    if (i % 2 == 0):
        print(string[i])
