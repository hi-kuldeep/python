marks  = input("Please enter your marks: ")
marks = int(marks)

if marks > 100:
    print(" Marks can't be greater than 100")
    exit()

if marks < 60:
    print("F")
elif marks <= 69:
    print("D")
elif marks <= 79:
    print("C")
elif marks <= 89:
    print("B")
else:
    print("A")
