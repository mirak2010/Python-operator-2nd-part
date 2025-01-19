height=float(input("Please enter your height in m, don't put the sign of measure: "))
weight=float(input("Please enter your weight in kg, don't put the sign of measure: "))
bmi=weight/ (height)**2
if bmi<=18.4:
    print("You are underweight!")
elif bmi<=24.9:
    print("You are healthy!")
elif bmi<=29.9:
    print("You are overweight!")
elif bmi<=34.9:
    print("You are severely overweight!")
elif bmi<=39.9:
    print("You are severely obese!")
else:
    print("Go home!")
