# Remove first n characters from the string

def remove_char (string,n):
    print(string[n::])

string = input("Enter a string: ")
n = int(input("Enter the value for n: "))
remove_char(string,n)
