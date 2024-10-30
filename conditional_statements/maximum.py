a, b, c = map(int, input("Enter a, b, c: ").split(","))

maximum = a

if b > maximum:
    maximum = b

if c > maximum:
    maximum = c

print("Maximum is:", maximum)