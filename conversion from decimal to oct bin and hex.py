# Python Program to Convert Decimal to Binary, Octal and Hexadecimal

def conversion (dec):
    print("Binary conversion = ",bin(dec))
    print("Octal conversion = ",oct(dec))
    print("Hexadecimal conversion = ",hex(dec))
    

dec = int(input("Enter a number to the base 10 = "))
conversion(dec)
