# age = int(input("enter your age: "))

# if age >= 18:
#     print("You Are Eligible For Movie Ticket")

# else:
#     print("You Are Not Eligible")

# practice que

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

if (age >= 18):
    print(f"{name} you are eligible for vote")


else:
    print (f"{name} you are not eligible for vote")
    c = 18 - age
    print (f"you will eligible after {c} years")