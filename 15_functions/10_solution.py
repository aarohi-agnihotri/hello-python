# RECURSIVE FUNCTION
# a function that calls itself until it hits a base case

def factorial(num):
    # base case 1 — stop recursion, invalid input
    if num < 0:
        return "not possible"
    # base case 2 — factorial(0) = 1, factorial(1) = 1
    # num in (0,1) checks if num exists in this tuple
    elif num in (0,1):
        return 1
    # recursive case — function calls itself with smaller value
    # factorial(5) = 5 * factorial(4)
    #              = 5 * 4 * factorial(3)
    #              = 5 * 4 * 3 * factorial(2)
    #              = 5 * 4 * 3 * 2 * factorial(1) → hits base case, returns 1
    #              = 5 * 4 * 3 * 2 * 1 = 120
    else:
        return num * factorial(num-1)

num = int(input("enter a number: "))
print(f"Factorial of {num} : {factorial(num)}")