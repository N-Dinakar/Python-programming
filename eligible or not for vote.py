age=int(input("Enter the age of the person:"))
if age>17:
    print("The person is eligible to vote")
else:
    print("The person not eligible to vote")
    print("The person needs to wait",18-age,"years to become eligible")
