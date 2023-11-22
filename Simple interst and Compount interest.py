# Simple Interest and Compound Interest Calculator

def simple_interest (p,t,r):
    si = ((p*t*r)/100)
    print("Simple interest: ",si)

def compound_interest (p,t,r):
    amt = p*(pow((1 + r/100),t))
    ci = amt - p
    print("Compound interest: ",ci)

p = int(input("Principal: "))
t = float(input("Time period: "))
r = float(input("Rate of interest: "))

simple_interest(p,t,r)
compound_interest(p,t,r)
