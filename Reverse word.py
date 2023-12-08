# Python code to reverse a given string and check whether the given word is a palindrome or not.
word = input("Enter any word: ")
rev = word[::-1]
print("Reversed word: ",rev)
if rev == word:
    print("The given word is a palindrome.")
else:
    print("The given word is not a palindrome")
