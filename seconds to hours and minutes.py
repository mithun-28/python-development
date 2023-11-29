# Python program to convert Seconds into Hours and Minutes in Python

def seconds_to_hr_and_mins (seconds):
    print(seconds,"Seconds = ",(seconds/3600),"Hours")
    print(seconds,"Seconds = ",(seconds/60),"Minutes")

seconds = float(input("Enter the value for seconds: "))
seconds_to_hr_and_mins (seconds)
