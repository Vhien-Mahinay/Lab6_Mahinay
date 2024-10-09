age = int(input("Enter your Age:"))
member = (input("Enter Yes or No if you have membership:"))

if age < 18:
    if member == "Yes":
        print("Total fee is 450.00 php")
    if member == "No":
        print("Total fee is 650.00 php")
elif age >= 18 and age <= 65:
    if member == "Yes":
        print("Total fee is 550.00 php")
    if member == "No":
        print("Total fee is 750.00 php")
elif age > 65:
    if member == "Yes":
        print("Total fee is 400.00 php")
    if member == "No":
        print("Total fee is 600.00 php")
        
        
    

    