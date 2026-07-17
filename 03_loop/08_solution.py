while True:
    user_input = int(input("Enter a number to check if it is prime or not: "))
    if user_input <= 1:
        print("Please enter number greater than 1")
    else:
        break

is_prime = True

for i in range(2, user_input):
    if (user_input % i) == 0:
        is_prime = False
        break

if is_prime:
    print(f"Your enter number {user_input} is prime number")
else:
    print(f"Your enter number {user_input} is not a prime number")
