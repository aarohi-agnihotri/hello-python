#-------manual program if don't know how many inputs a function will recieve, here we use array----------
# def func(nums):
#     length = len(nums) #finding length
#     for i in range(length):
#         print(nums[i])

#     # more better -
#     # for i in nums:
#     #     print(i)


# func([5,10,15,20,25]) # using array- user has to manually wrap in []

# ----------better way to use *, args, so user dont have to manually add []-------

#-------basic program, use of *args-------
def func(*args):
    return sum(args) # sum() is method which calculates sum and return total

print(func(10,22,33))
print(func(3,56,23,45,67))

# ----changing name, but not recommend--------
# def func(*chai):
#     return sum(chai)

# print(func(10,22,33))
# print(func(3,56,23,45,67))

# --------diff btw print(*args) and print(args)--------
# def func(*args):
#     print(*args)
#     # print(args)
#     return sum(args)

# print(func(10,22,33))
# print(func(3,56,23,45,67))

#------loop example, priting 2's table--------
# def func(*args):
#     for arg in args:
#         print(arg*2)

# func(1,2,3,4,5,6,7,8,9,10)

#----multiplying example-----
# def func(*args):
#     result = 1
#     for i in args:
#         result *= i
#     return result

# print(func(3,4,5))