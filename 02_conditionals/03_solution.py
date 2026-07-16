marks  = input("Please enter your marks: ")
marks = int(marks)

# Not allowed to enter more than 100
if marks > 100:
    print(" Marks can't be greater than 100")
    exit()

# 60-  69   D
# 70-  79   C
# 80-  89   B
# 90- 100   A

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
