num = int(input("Enter a number: "))

a = 0
b = 1

while a <= num:
    if a == num:
        print("It is a Fibonacci number")
        break
    a, b = b, a + b
else:
    print("Not a Fibonacci number")