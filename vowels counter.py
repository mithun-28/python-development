# Function to count number of vowels in the string

def vowels_counter (string):
    count = 0
    for i in string:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            count = count + 1
    return count


string = input("Enter any string: ")
print("Total number of vowels in the string = ",vowels_counter(string))
