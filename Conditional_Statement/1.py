age = 20
citizen = "INDIAN"

if age >= 18:
    print("Age criteria satisfied")

    if citizen == "INDIAN":
        print("You are eligible to vote in INDIA")
    else:
        print("You must be INDIAN  to vote ")

else:
    print("You are not eligible to vote because your age is below 18")