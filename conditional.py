#if-else statements
#simple if else

age = 18
if age>=18:
    print("you are in adult")
else:
    print("you are minor")

    #multiple conditions
marks = 75
if marks>= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >=60:
    print("Grade C")
else:
    print("Grade:F")

#CHECK NUMBER

number = 10
if number > 0:
    print("Positive number")
elif number<0:
    print("Negative number")
else:
    print("Zero")

#logical operators
age = 25
has_license = True
if age >= 18 and has_license:
    print("you can drive")
else:
    print("you cannot  drive")