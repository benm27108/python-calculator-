#PYTHON WEIGHT CALCULATOR

weight = float(input("Enter your weight"))
unit = input("Kilogram or Pounds (Kgs, Lbs): ")

if unit == "Kgs":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {weight},{unit}")
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {weight},{unit}")
else:
    print(f"{unit} is not valid")

