# Vete eligibility checker

def check_eligibility (name,age):
    if age >= 18:
        print(name.upper(),"is eligible to vote!")
    else:
        print(name.upper(),"is not eligible to vote!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
check_eligibility(name,age)
