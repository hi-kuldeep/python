age = input("Enter your age: ")
day = input("Enter the day: ").lower()
age = int(age)
price = 12 if age >= 18 else 8

message = "Your age is {} so according to that ticket price is ${}"

if day == "wednesday" or day == "wed":
    price -= 2

message = message.format(age , price)

print(message)