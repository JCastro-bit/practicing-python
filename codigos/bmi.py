#your code goes here


def convert(weight,height):
    bmi = weight / (height)**2
    if bmi <= 18.4:
        print("Underweight")
    elif bmi <= 24.9:
        print("Normal")
    elif bmi <= 29.9:
        print("Overweight")
    elif bmi >= 30:
        print("Obesity")
    else:
        print("You are severely obese.")

result1 = convert(52,1.85)
result2 = convert(130,1.7)