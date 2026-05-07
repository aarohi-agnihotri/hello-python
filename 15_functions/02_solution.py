# ============================================================
# FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================
# (num_one, num_two) → two parameters separated by comma
# when calling → add(first_num, second_num)
#                first_num maps to num_one
#                second_num maps to num_two
# order matters! arguments are assigned by position
# ============================================================

def add(num_one, num_two):
    return num_one + num_two

first_num = int(input("enter first number: "))
second_num = int(input("enter second number: "))
print(f"sum of {first_num} and {second_num} : {add(first_num, second_num)}")
# add(first_num, second_num) → called inside f-string directly, return value used as output