# Python function to check whether the string contains equal number of "X" and "O"
def count_x_o (string):
    count_x = 0
    count_o = 0
    for i in string:
        if i == "x" or i == "X":
            count_x += 1
        elif i == "o" or i == "O":
            count_o += 1
    if count_x == count_o:
        return True
    else:
        return False


string = input("Enter a string: ")
print(count_x_o(string))
