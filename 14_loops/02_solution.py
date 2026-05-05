n = int(input("enter value of n: "))
sum_even = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_even += i

for i in range(2, n+1, 2):
    # print(i)
    sum_even += i

print("Sum of even numbers are", sum_even)  