while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        break
    else:
        print("Invalid input, Please try again!")
        
print("You entered ", number)
print("Your input registered successfully! - Thank you")
    