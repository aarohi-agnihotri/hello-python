# ============================================================
# FUNCTIONS IN PYTHON
# ============================================================
# def       → keyword to define a function, creates a reusable block of code called a function
# square_of_num → function name
# (number)  → parameter (input the function accepts)
# return    → sends result back to the caller
#             without return, function gives nothing back (None)
# ============================================================


# ============================================================
# WHY return OVER print INSIDE FUNCTION?
# ============================================================
# print inside function (old way):
#     def square_of_num(number):
#         print(number ** 2)      # just displays, cant use result later
#
# square_of_num(4)  → calling function with argument 4
#                     argument is the actual value passed when calling
#                     parameter is the variable in function definition (number)
#                     so parameter = number, argument = 4
# return (better way):
#     def square_of_num(number):
#         return number ** 2      # sends result back, can store and reuse
# ============================================================


def square_of_num(number):
    result = number ** 2
    return result                 # returns result back to caller

number = int(input("Input number: "))
print("Square of", number, ":", square_of_num(number))  # function called here, return value used directly in print