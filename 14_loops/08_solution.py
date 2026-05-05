num = int(input("enter a number: "))
# count = 0
is_prime = True

if num < 1:
    print("Plz enter positive number greater than 1 !!")
    exit()
else:
    for i in range(2, num//2):
        if num % i == 0:
            # count += 1
            is_prime = False
            break

    # if count != 0: print(num, "is not a prime number")
    # else: print(num, "is a prime number")

    if is_prime: print(num, "is a prime number")
    else: print(num, "is not a prime number")

# range() needs int, // gives int directly unlike / which gives float (e.g 5 vs 5.0)
# +1 because stop is not included in range, but for most cases it won't matter
# because if num is divisible by half, it's already divisible by 2 which is caught earlier