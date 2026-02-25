num = int(input("Enter a number: "))

i = 1
fact = 1

while fact < num:
    i += 1
    fact *= i

if fact == num:
    print("It is a Factorial number")
else:
    print("Not a Factorial number")