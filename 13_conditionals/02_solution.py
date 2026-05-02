# ============================================================
# ORIGINAL CODE (Commented Out)
# ============================================================

# age = int(input("enter your age \n")) 
# day = input("enter today's day \n")
# print("Your movie ticket's price : ")

# if(day == "wed"):       
#     if age < 18:
#         print("$", 8-2) # BUG: hardcoded math, discount applied in wrong branch
#     else:
#         print("$", 12-2)
# else:
#     if age < 18:
#         print("$8")      # No discount applied here (logic was flipped)
#     else:
#         print("$12")

# ============================================================
# IMPROVEMENTS MADE
# ============================================================
# 1. Instead of asking day name, simply ask yes/no for Wednesday (avoids spelling/casing issues)
# 2. Used ternary operator to set base price in a single clean line
# 3. Applied discount separately using -= 2 instead of hardcoding 8-2 or 12-2
# 4. Used f-string for clean and readable output
# ============================================================

# CORRECTED & OPTIMIZED CODE
# ============================================================

age = int(input("enter your age: "))
is_wednesday = (input("Is today wednesday? enter yes or no : ")).strip().lower()

price = 12 if age >= 18 else 8

if is_wednesday in ["yes", "y"]:
    price -= 2

print(f"Your ticket's price is: ${price}")