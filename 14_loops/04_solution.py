input_str = input("Input a string: ")
reversed_str = ""
len_str = len(input_str)
# print(len_str)

for char in range(len_str-1, -1, -1): #start from last index, stop at 0 (included)
    reversed_str += input_str[char]       
    
print("Reversed string:", reversed_str)

print("-----Second Way------")
reversed_str2 = ""
for char in input_str:
    reversed_str2 = char + reversed_str2  #optimised

print("Reversed string:", reversed_str2)

# ---------- Previous code --------------

# input_str = input("Input a string: ")
# reversed_str = ""
# len_str = len(input_str)

# for char in range(len_str, 0, -1):  # BUG: starts at len_str but last valid index is len_str-1, causes index out of range
#     reversed_str += input_str[char]
#     print(reversed_str)               # BUG: print should be outside loop, prints after every letter instead of once

# ============================================================
# IMPROVEMENTS MADE
# ============================================================
# 1. Fixed range: changed range(len_str, 0, -1) to range(len_str-1, -1, -1) to avoid index out of range
# 2. Moved print outside the loop to print final reversed string once
# ============================================================
