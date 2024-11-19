# Rekursiya

'''factorial(n): n = 5

5! = 5 * 4! 1 5!
4! = 4 * 3! 2
3! = 3 * 2! 3
2! = 2 * 1! 4 -> 2! = 2 * 1 = 2
1! = 1 * 0! 5 -> 1! = 1 * 1 = 1
0! = 1 6

start midpoint endpoint'''

def factorial_recursion(n): #n = 5, 4, 3, 2, 1, 0
    if n == 0:
        return 1

    return n * factorial_recursion(n - 1) #5 * 24, 4 * 6, 3 * 2, 2! = 2 * 1, 1! = 1 * 1

#print(factorial_recursion(5))

# reference vs value

def change_number(n): # copy of original (n)
    n += 5
    print("Inside function", n)

def change_list(l):
    l += [5] # 1, 2, 3 -> 1, 2, 3, 5
    print("Inside function", l)


'''n = 7 // 4 bayt

change_number(n)

print("Outside function", n)'''

my_list = [1, 2, 3] # 4m bayt

change_list(my_list)

print("Outside function", my_list)


# int, float 0x34374F -> 7
