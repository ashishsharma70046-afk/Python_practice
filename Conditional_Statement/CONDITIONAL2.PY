

# ---------------------IF STSTEMENT---------------------------------------
# example => 1

age = 20

if age >= 18:
    print("You are eligible to vote")
print("---------------------------------------------------------------------------------")


# example => 2

marks = 75

if marks >= 33:
    print("You are passed")
print("----------------------------------------------------------------------------------")


# ------------------------IF-ELSE STATEMENT------------------------------------------------------

# example => 1

age = 20

if age >= 18:
    print("Adult")
else:
    print("Not Adult")
print("---------------------------------------------------------------------------------------------")

# example => 2

num = 5

if num > 0:
    print("Positive")
else:
    print("Negative")

print("--------------------------------------------------------------------------------------------------")

# -----------------------------------IF ELIF STATEMENT----------------------------------------------------------------







# example => 1

temp = 30

if temp > 40:
    print("Very Hot")
elif temp > 25:
    print("Hot")
elif temp > 15:
    print("Normal")

print("--------------------------------------------------------------------------------------------------------")

# example => 2

day = 2

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")

print("--------------------------------------------------------------------------------------------------")

# ---------------------------------------NASTED STSTEMENT-------------------------------------------------------

# example => 1. 

marks = 80

if marks >= 33:
    if marks >= 60:
        print("First Division")
    else:
        print("Pass")
else:
    print("Fail")

print("------------------------------------------------------------------------------------------------------------")

# example =>2. 

age = int(input("Enter your age: "))
citizen = input("Enter your citizenship: ")

if age >= 18:
    if citizen == "INDIAN":
        print("Eligible to vote")
    else:
        print("Not an Indian citizen")
else:
    print("Age is below 18")
