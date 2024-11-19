#Sual 1: Verilən bir ədədi yalnız 1 və özündən başqa böləni yoxdursa,  (yəni sadə ədəddirsə) "Sadədir" 
# yazdırın. Əks halda, "Sadə deyil" yazdırın.

n = int(input("Enter the number: "))

for i in range(2, n):
    if n % i == 0:
        print("Sade deyil")
        
        break
else:
    print("Sadedir")

#Sual 2: Verilən bir ədədin rəqəmlərinin cəmini tapın. Məsələn, 123 üçün cəmi 6 (1 + 2 + 3) olmalıdır.
# (İpucu: While, %, // istifadə edə bilərsiniz)

n = int(input("Enter the number: "))

digits_sum = 0

while n > 0:
    digits_sum += n % 10
    
    n //= 10
    
print(digits_sum)

#Ulduzlar meselesi 1

n = int(input("Enter the number: "))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
        
    print()
    
# practice1 fayli:
# Task 1

a = int(input("Enter base: "))

x = int(input("Enter exponent: "))

degree = 1

for i in range(x):
    degree *= a

print(degree)

# Task 2

for i in range(1, 51):
    if i % 2 == 0:
        print(i)
        
# Task 3

n = int(input())

sum_ = 0

for i in range(1, n + 1):
    sum_ += i
    
print(sum)

#task 4

x, n = map(int, input().split())

k = 1

sum_ = 0

for i in range(n + 1):
    sum_ += k * x ** n
    
    k *= -1

# Task 5

for i in range(11):
    print(i, i ** 2)

# Task 6

even_sum = 0

odd_product = 1

for i in range(11):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_product *= i


print("Sum:", even_sum)

print("Product:", odd_product)

# Task 7

for i in range(10000, 100000):
    if i % 133 == 125 and i % 134 == 111:
        print(i)
        
# Task 8

a, b = map(int, input().split())

min_ = a

if b < min_:
    min_ = b
    
for i in range(1, min_ + 1):
    if a % i == 0 and b % i == 0:
        ebob = i
        
print(ebob)

# Task 9

for i in range(5, 11):
    if i == 7 or i == 9:
        continue

    print(i)
    
# ulduzlar 2

n = int(input())

for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
        
    for j in range(2 * i + 1):
        print('*', end='')
    
    print()